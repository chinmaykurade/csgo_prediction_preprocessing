# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 20:14:00 2020

@author: chinm
"""



def clean_rest(df): 
    dropcols = ['current_score','active_smokes', 'active_molotovs', \
            'previous_kills','planted_bomb', 'C4_ct',\
            'players','Knife_t','Knife_ct', 'pos_t1', 'pos_t2', 'pos_t3',\
            'pos_t4', 'pos_t5', 'pos_ct1', 'pos_ct2', 'pos_ct3', 'pos_ct4',\
            'pos_ct5', 'smoke_1', 'smoke_2', 'smoke_3', 'smoke_4', 'smoke_5',\
            'molotov_1', 'molotov_2', 'molotov_3', 'molotov_4', 'molotov_5',\
            'kill1weapon', 'kill1attacker_side', 'kill1attacker_position',\
            'kill1victim_side', 'kill1victim_position', 'kill2weapon',\
            'kill2attacker_side', 'kill2attacker_position', 'kill2victim_side',\
            'kill2victim_position', 'kill3weapon', 'kill3attacker_side', \
            'kill3attacker_position', 'kill3victim_side', 'kill3victim_position',\
            'kill4weapon', 'kill4attacker_side', 'kill4attacker_position',\
            'kill4victim_side', 'kill4victim_position', 'kill5weapon',\
            'kill5attacker_side', 'kill5attacker_position', 'kill5victim_side',\
            'kill5victim_position', 'kill6weapon', 'kill6attacker_side',\
            'kill6attacker_position', 'kill6victim_side', 'kill6victim_position',\
            'kill7weapon', 'kill7attacker_side', 'kill7attacker_position',\
            'kill7victim_side', 'kill7victim_position', 'kill8weapon',\
            'kill8attacker_side', 'kill8attacker_position', 'kill8victim_side',\
            'kill8victim_position', 'kill9weapon', 'kill9attacker_side',\
            'kill9attacker_position', 'kill9victim_side', 'kill9victim_position',\
            'kill10weapon', 'kill10attacker_side', 'kill10attacker_position',\
            'kill10victim_side', 'kill10victim_position']
    df.drop(columns=dropcols,inplace=True)
    
    return df