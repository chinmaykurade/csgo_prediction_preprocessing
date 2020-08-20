 #!/usr/bin/python

import sys
import pickle
import pandas as pd
import preprocess_all_v2 as pal
from sklearn.preprocessing import StandardScaler
from columns import colwep,colpla,maps,all_round_status

# print('Number of arguments:', len(sys.argv), 'arguments.')
arg_list = list(sys.argv)
# print('Argument List:', arg_list)

input_path = arg_list[1]
output_path = arg_list[2]
current_path = arg_list[3]
# print(out_path)

print('Reading and Procesing input data...')
dft = pd.read_json(input_path)
dft = pal.pre_fea(dft,colpla,colwep,maps,all_round_status)
# dft.to_csv('D:/Code/csgo_prediction/datasets/inp.csv')


print('Predicting and Writing output data...')
model_data = pickle.load(open(current_path+'/best_model_v2.pickle','rb'))

cols = model_data['columns']
clf = model_data['clf']
scaler = model_data['scaler']

X_data = dft[cols]
X_data = scaler.fit_transform(X_data)

Y_data = clf.predict(X_data)
temp = pd.DataFrame(Y_data,columns=['round_winner'])
# temp.to_json('temp.json')
Y_final = pd.DataFrame(temp['round_winner'].apply(lambda x:'Terrorist' if x==1 else 'CT'),columns=['round_winner'])
Y_final.to_json(output_path,orient='records')