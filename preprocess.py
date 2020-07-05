# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 09:50:02 2020

@author: chinm
"""

import pandas as pd
import preprocess_step_functions as psf
import time
import os
from columns import colwep,colkills,colpla,colpos,maps,all_round_status,\
colsmokes,colmolotov,colmapbs,colbs,colpr,colhurt

##############################################################################

def preprocess(input_dir,output_dir):
    for i in range(len(os.listdir(input_dir))):
        path = input_dir+"dataset_{:02}.json".format(i)
        print("Processing : {}".format(path))
        dft = pd.read_json(path)
        dft = psf.position_and_Individual_stats(dft,colpla,colwep,colpos,maps,\
                                                all_round_status)
        dft = psf.kills_smokes_molotovs(dft,colsmokes,colmolotov,colkills)
        dft = psf.proximity_players(dft,colpr)
        dft = psf.pos_bs(dft,colbs,maps,colmapbs)
        dft = psf.kill_features(dft,colhurt)
        dft.to_json(output_dir+"dataset_{:02}.json".format(i))

###############################################################################

tic = time.time()

input_dir = "datasets/dataset_initial/"
#input_dir = "datasets/dataset_processed/"
output_dir = "datasets/dataset_processed/"
if(not os.path.exists(output_dir)):
    os.mkdir(output_dir)
preprocess(input_dir,output_dir)

toc = time.time()

print(toc-tic)

###############################################################################
#colkills = ['kill_1_weapon','kill_1_attacker_position','kill_1_attacker_side',\
#            'kill_1_victim_position','kill_1_victim_side',\
#            'kill_2_weapon','kill_2_attacker_position','kill_2_attacker_side',\
#            'kill_2_victim_position','kill_2_victim_side',\
#            'kill_3_weapon','kill_3_attacker_position','kill_3_attacker_side',\
#            'kill_3_victim_position','kill_3_victim_side',\
#            'kill_4_weapon','kill_4_attacker_position','kill_4_attacker_side',\
#            'kill_4_victim_position','kill_4_victim_side',\
#            'kill_5_weapon','kill_5_attacker_position','kill_5_attacker_side',\
#            'kill_5_victim_position','kill_5_victim_side']

#colpla = ['health_t1','health_t2','health_t3','health_t4','health_t5',\
#        'health_ct1','health_ct2','health_ct3','health_ct4','health_ct5',\
#        'money_t1','money_t2','money_t3','money_t4','money_t5',\
#        'money_ct1','money_ct2','money_ct3','money_ct4','money_ct5',\
#        'armor_t1','armor_t2','armor_t3','armor_t4','armor_t5',\
#        'armor_ct1','armor_ct2','armor_ct3','armor_ct4','armor_ct5',\
#        'defuse_kit_ct1','defuse_kit_ct2','defuse_kit_ct3','defuse_kit_ct4','defuse_kit_ct5',\
#        'has_helmet_t1','has_helmet_t2','has_helmet_t3','has_helmet_t4','has_helmet_t5',\
#        'has_helmet_ct1','has_helmet_ct2','has_helmet_ct3','has_helmet_ct4','has_helmet_ct5',\
#        ]