# -*- coding: utf-8 -*-

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

maps = ['map_de_dust2', 'map_de_inferno', 'map_de_mirage', 'map_de_nuke', \
        'map_de_overpass', 'map_de_train', 'map_de_vertigo','map_de_cache']

all_round_status = ['round_status_BombPlanted', 'round_status_FreezeTime', \
                    'round_status_Normal']

colmapbs = ['de_cache_A', 'de_dust2_A', 'de_inferno_A', 'de_mirage_A', \
            'de_nuke_A','de_overpass_A', 'de_train_A', 'de_vertigo_A',\
            'de_cache_B', 'de_dust2_B','de_inferno_B', 'de_mirage_B', \
            'de_nuke_B','de_overpass_B', 'de_train_B','de_vertigo_B']

###############################################################################