# -*- coding: utf-8 -*-

import pandas as pd
import time
import os
import preprocess_all_v2 as pal
from columns import colwep,colpla,maps,all_round_status

def preprocess(input_dir,output_dir):
    for i in range(len(os.listdir(input_dir))):
        path = input_dir+"dataset_{:02}.json".format(i)
        print("Processing : {}".format(path))
        dft = pd.read_json(path)
        dft = pal.pre_fea(dft,colpla,colwep,maps,all_round_status)
        dft.to_json(output_dir+"dataset_{:02}.json".format(i))

###############################################################################

tic = time.time()

input_dir = "datasets/dataset_initial/"
output_dir = "datasets/dataset_processed_v2/"
if(not os.path.exists(output_dir)):
    os.mkdir(output_dir)
preprocess(input_dir,output_dir)

toc = time.time()

print(toc-tic)