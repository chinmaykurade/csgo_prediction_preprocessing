# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 07:05:00 2020

@author: chinm
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import os

pd.set_option('max_columns', None)
drop_rest = True

## Some helper functions
def binn(dft,num_bin = 10):
    interval = (dft.max()-dft.min())/(num_bin)
    interval += interval*0.01
    new_dft = dft.copy()-dft.min()
    new_dft = new_dft//interval
    return new_dft

def save_json(df,output,split=5000):
    if(not os.path.exists(output)):
        os.mkdir(output)
    df=df.reindex()
    total = len(df)
    left = total
    i = 0
    while left>0:
        dft = df[split*i:split*(i+1) if left>split else split*i+left].copy()
        dft.to_json(output+"dataset_{:02}.json".format(i))
        i += 1
        left = left-split

def read_all(template,start,end):
    frames = [ pd.read_json(f).fillna(0) for f in [template.format(i) \
                                                   for i in range(start,end)]]
    X = pd.concat(frames, ignore_index = True,sort = True)
    return X
###############################################################################

# Importing the dataset
template = "datasets/dataset_cleaned/dataset_{:02}.json"
num_datasets = len(os.listdir('datasets/dataset_cleaned/'))
df = read_all(template,0,num_datasets)

if 'index' in list(df.columns): df.drop(columns='index',inplace=True,axis=1) 

## Get the y data
df['round_winner_t'] = df['round_winner'].apply(lambda x: 0 if x=='CT' else 1)
df = df.drop('round_winner',axis=1)

## Difference in current_score
df['t_leads'] = df['current_score_t'] - df['current_score_ct']

## Total defuse kits and helmets
df['defuse_kit_ct'] = df['defuse_kit_ct1'] + df['defuse_kit_ct2'] + \
    df['defuse_kit_ct3'] + df['defuse_kit_ct4'] + df['defuse_kit_ct5']
    
df['has_helmet_ct'] = df['has_helmet_ct1'] + df['has_helmet_ct2'] + \
    df['has_helmet_ct3'] + df['has_helmet_ct4'] + df['has_helmet_ct5']
    
df['has_helmet_t'] = df['has_helmet_t1'] + df['has_helmet_t2'] + \
    df['has_helmet_t3'] + df['has_helmet_t4'] + df['has_helmet_t5']

## Checking for multicolinearity
# dfcorr = df.corr()

# for idx,col in enumerate(list(dfcorr.columns)):
#     for i in range(len(dfcorr[col])):
#         if(dfcorr[col][i] > 0.95 or dfcorr[col][i] < -0.95):
#             if(idx!=i):
#                 print(col,dfcorr.index[i]," : {}".format(dfcorr[col][i]))

# We can see that alive_players_t,health_t and alive_players_ct and health_ct 
# are highly correlated(correlation factor = 0.956)
# print(pd.pivot_table(df,index = 'alive_players_ct',values = 'health_ct'))
# print(pd.pivot_table(df,index = 'alive_players_t',values = 'health_t'))

# df.drop(columns = ['health_t','health_ct'],inplace=True,axis=1)

# handle case when alive players for a team > 5
idxs_t = df['alive_players_t'][np.array(list(df['alive_players_t'].\
          apply(lambda x: 1 if x>5 else 0)))==1]
idxs_ct = df['alive_players_ct'][np.array(list(df['alive_players_ct'].\
          apply(lambda x: 1 if x>5 else 0)))==1]

## Clearly, this is a glitch and must be omitted from he dataset  
df.drop(index=idxs_t.index,inplace=True)
df.drop(index=idxs_ct.index,inplace=True)


## binning for continuous variables
colcon = ['armor_ct', 'armor_ct1', 'armor_ct2', 'armor_ct3', 'armor_ct4',\
           'armor_ct5', 'armor_t', 'armor_t1', 'armor_t2', 'armor_t3',\
           'armor_t4', 'armor_t5', 'health_ct1', 'health_ct2',\
           'health_ct3', 'health_ct4', 'health_ct5', 'health_t1',\
           'health_t2', 'health_t3', 'health_t4', 'health_t5',\
           'health_t','health_ct']

colconq = ['money_ct','money_ct1', 'money_ct2', 'money_ct3', 'money_ct4', \
           'money_ct5','money_t', 'money_t1', 'money_t2', 'money_t3', \
           'money_t4','money_t5']


for col in colcon:
    df[col+'_Bin_Code'] = binn(df[col])  #10 bins for all

# Quantized bins for money since it is not reset
label = LabelEncoder()
for col in colconq:
    try:
        df[col+'_Bin'] = pd.qcut(df[col].astype(int),10,duplicates='drop')
    except ValueError:
        print("Binning failed for : %s" %(col))
        continue
    df[col+'_Bin_Code'] = label.fit_transform(df[col+'_Bin'])
  

if(drop_rest):
    df.drop(columns=colcon+colconq,inplace=True,axis=1)
    df.drop(columns=[col+'_Bin' for col in colconq],inplace=True,axis=1)
  
output_dir = "datasets/dataset_finalized/"
save_json(df,output_dir)
##################
#
#df[['current_score_t','current_score_ct','t_leads','round_winner_t']].corr()
#
#pd.pivot_table(df,index = 'M4a4_ct',values = 'round_winner_t')
#
#df['M4a4_ct'].hist()
#
#pd.pivot_table(df,index = 'money_ct1',values = 'round_winner_t')
