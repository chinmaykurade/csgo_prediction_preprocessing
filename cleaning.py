# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 20:05:21 2020

@author: chinm
"""
import os
import pandas as pd
import cleaning_weapons as clw
import cleaning_rest as clr

def clean(input_dir,output_dir):
    for i in range(len(os.listdir(input_dir))):
        path = input_dir+"dataset_{:02}.json".format(i)
        print("Processing : {}".format(path))
        dft = pd.read_json(path)
        dft = clw.clean_weapons(dft)
        print("Cleaned weapons...")
        dft = clw.clean_kill_weapons(dft)
        print("Cleaned kill weapons...")
        dft = clr.clean_rest(dft)
        print("Cleaned rest...Saving now.")
        dft.to_json(output_dir+"dataset_{:02}.json".format(i))
        
input_dir = "datasets/dataset_processed/"
output_dir = "datasets/dataset_cleaned/"
#os.mkdir(output_dir)
clean(input_dir,output_dir)