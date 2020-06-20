# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 09:50:02 2020

@author: chinm
"""

import pandas as pd
import preprocess_step_functions as psf
import time
import os

##############################################################################

def create_colpla():
    listpla = []
    for i in range(5):
        listpla.append('health_t'+str(i+1))
        listpla.append('health_ct'+str(i+1))
        listpla.append('armor_t'+str(i+1))
        listpla.append('armor_ct'+str(i+1))
        listpla.append('money_t'+str(i+1))
        listpla.append('money_ct'+str(i+1))
        listpla.append('has_helmet_t'+str(i+1))
        listpla.append('has_helmet_ct'+str(i+1))
        listpla.append('defuse_kit_ct'+str(i+1))
    return listpla

def create_colkills(n):
    listkill = []
    for i in range(n):
        listkill.append('kill'+str(i+1)+'weapon')
        listkill.append('kill'+str(i+1)+'attacker_side')
        listkill.append('kill'+str(i+1)+'attacker_position')
        listkill.append('kill'+str(i+1)+'victim_side')
        listkill.append('kill'+str(i+1)+'victim_position')
    return listkill

def preprocess(input_dir,output_dir):
    for i in range(len(os.listdir(input_dir))):
        path = input_dir+"dataset_{:02}.json".format(i)
        print("Processing : {}".format(path))
        dft = pd.read_json(path)
        dft = psf.position_and_Individual_stats(dft,colpla,colwep,colpos,maps,all_round_status)
        dft = psf.kills_smokes_molotovs(dft,colsmokes,colmolotov,colkills)
        dft = psf.proximity_players(dft)
        dft = psf.pos_bs(dft,colbs,maps,colmapbs)
        dft.to_json(output_dir+"dataset_{:02}.json".format(i))

###############################################################################

colwep = "Deagle, Elite, FiveSeven, Glock, Ak47, Aug, Awp, Famas, G3sg1, \
GalilAr, M249, M4a4, Mac10, P90, Mp5sd, Ump45, Xm1014, Bizon, Mag7, Negev, \
Sawedoff, Tec9, ZeusX27, P2000, Mp7, Mp9, Nova, P250, Scar20, Sg553, Ssg08, \
M4a1S, UspS, Cz75Auto, R8Revolver, Flashbang, HeGrenade, SmokeGrenade, \
MolotovGrenade, DecoyGrenade, IncendiaryGrenade, Knife, C4".split(', ')

colpla = create_colpla()

colpos = ['pos_t1','pos_t2','pos_t3','pos_t4','pos_t5',\
        'pos_ct1','pos_ct2','pos_ct3','pos_ct4','pos_ct5']

maps = ['map_de_dust2', 'map_de_inferno', 'map_de_mirage', 'map_de_nuke', \
        'map_de_overpass', 'map_de_train', 'map_de_vertigo','map_de_cache']

all_round_status = ['round_status_BombPlanted', 'round_status_FreezeTime', \
                    'round_status_Normal']

colsmokes = ['smoke_1','smoke_2','smoke_3','smoke_4','smoke_5']

colmolotov = ['molotov_1','molotov_2','molotov_3','molotov_4','molotov_5']

colkills = create_colkills(10)

colmapbs = ['de_cache_A', 'de_dust2_A', 'de_inferno_A', 'de_mirage_A', \
            'de_nuke_A','de_overpass_A', 'de_train_A', 'de_vertigo_A',\
            'de_cache_B', 'de_dust2_B','de_inferno_B', 'de_mirage_B', \
            'de_nuke_B','de_overpass_B', 'de_train_B','de_vertigo_B']

colbs = ['pos_bs_t1','pos_bs_t2','pos_bs_t3','pos_bs_t4','pos_bs_t5',\
        'pos_bs_ct1','pos_bs_ct2','pos_bs_ct3','pos_bs_ct4','pos_bs_ct5']

###############################################################################

tic = time.time()

input_dir = "datasets/dataset_initial/"
output_dir = "datasets/dataset_processed/"
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