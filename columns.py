# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:59:01 2020

@author: chinm
"""

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
        listkill.append('kill'+str(i+1)+'attacker_position')
        listkill.append('kill'+str(i+1)+'attacker_side')
        listkill.append('kill'+str(i+1)+'victim_position')
        listkill.append('kill'+str(i+1)+'victim_side')
    return listkill

###############################################################################

colwep = "Deagle, Elite, FiveSeven, Glock, Ak47, Aug, Awp, Famas, G3sg1, \
GalilAr, M249, M4a4, Mac10, P90, Mp5sd, Ump45, Xm1014, Bizon, Mag7, Negev, \
Sawedoff, Tec9, ZeusX27, P2000, Mp7, Mp9, Nova, P250, Scar20, Sg553, Ssg08, \
M4a1S, UspS, Cz75Auto, R8Revolver, Flashbang, HeGrenade, SmokeGrenade, \
MolotovGrenade, DecoyGrenade, IncendiaryGrenade, Knife, C4".split(', ')

colhurt = colwep.copy()
colhurt.append('Inferno')
colhurt.append('World')

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


colpr = ['pr_t1','pr_t2','pr_t3','pr_t4','pr_t5','pr_ct1','pr_ct2','pr_ct3','pr_ct4','pr_ct5']

###############################################################################