# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 05:49:50 2020

@author: chinm
"""

import pandas as pd
import numpy as np
from tqdm import tqdm
# from sklearn.preprocessing import LabelEncoder
import preprocess_utils as pu

## Some helper functions
def binn(dft,num_bin = 10):
    interval = (dft.max()-dft.min())/(num_bin)
    interval += interval*0.01
    new_dft = dft.copy()-dft.min()
    new_dft = new_dft//interval
    return new_dft


def finalize(df):
    ## Get the y data
    df['round_winner_t'] = df['round_winner'].apply(lambda x: 0 if x=='CT' else 1)
        
    ## Handling the case when alive players > 5
    df['alive_players_t'] = df['alive_players_t'].apply(lambda x: 5 if x>5 else x)
    df['alive_players_ct'] = df['alive_players_ct'].apply(lambda x: 5 if x>5 else x)        
    return df

def pre_fea(dfpre,colpla,colwep,all_maps,all_round_status):
    for ds in [dfpre]:
        ds['alive_players_t']  = list(map(len ,pu.get_attr(ds, "Terrorist")))
        ds['alive_players_ct'] = list(map(len, pu.get_attr(ds, "CT")))
        ds['health_ct']        = list(map(sum, pu.get_attr(ds, "CT", "health")))
        ds['health_t']         = list(map(sum, pu.get_attr(ds, "Terrorist", \
                                                            "health")))
        ds['money_ct']         = list(map(sum, pu.get_attr(ds, "CT", "money")))
        ds['money_t']          = list(map(sum, pu.get_attr(ds, "Terrorist", \
                                                            "money")))
        ds['armor_ct']         = list(map(sum, pu.get_attr(ds, "CT", "armor")))
        ds['armor_t']          = list(map(sum, pu.get_attr(ds, "Terrorist", \
                                                            "armor")))
        ds['has_helmet_ct']    = list(map(sum, pu.get_attr(ds, "CT", "has_helmet")))
        ds['has_helmet_t']     = list(map(sum, pu.get_attr(ds, "Terrorist", \
                                                            "has_helmet")))
        ds['defuse_kit_ct']    = list(map(sum, pu.get_attr(ds, "CT", "has_defuser")))
        
    dfh_t = pu.get_attr(dfpre, "Terrorist", "health")
    dfh_t = pd.DataFrame(dfh_t,columns=['health_t1',\
           'health_t2', 'health_t3', 'health_t4', 'health_t5'])
    dfh_ct = pu.get_attr(dfpre, "CT", "health")
    dfh_ct = pd.DataFrame(dfh_ct,columns=['health_ct1',\
           'health_ct2', 'health_ct3', 'health_ct4', 'health_ct5'])
    dfm_t = pu.get_attr(dfpre, "Terrorist", "money")
    dfm_t = pd.DataFrame(dfm_t,columns=['money_t1', 'money_t2', 'money_t3', \
           'money_t4','money_t5'])
    dfm_ct = pu.get_attr(dfpre, "CT", "money")
    dfm_ct = pd.DataFrame(dfm_ct,columns=['money_ct1', 'money_ct2', 'money_ct3', \
           'money_ct4','money_ct5'])
    dfa_t = pu.get_attr(dfpre, "Terrorist", "armor")
    dfa_t = pd.DataFrame(dfa_t,columns=['armor_t1', 'armor_t2', 'armor_t3', \
           'armor_t4','armor_t5'])
    dfa_ct = pu.get_attr(dfpre, "CT", "armor")
    dfa_ct = pd.DataFrame(dfa_ct,columns=['armor_ct1', 'armor_ct2', 'armor_ct3', \
           'armor_ct4','armor_ct5'])
    dfhh_t = pu.get_attr(dfpre, "Terrorist", "has_helmet")
    dfhh_t = pd.DataFrame(dfhh_t,columns=['has_helmet_t1',\
           'has_helmet_t2', 'has_helmet_t3', 'has_helmet_t4', 'has_helmet_t5'],dtype=int)
    dfhh_ct = pu.get_attr(dfpre, "CT", "has_helmet")
    dfhh_ct = pd.DataFrame(dfhh_ct,columns=['has_helmet_ct1',\
           'has_helmet_ct2', 'has_helmet_ct3', 'has_helmet_ct4', 'has_helmet_ct5'],dtype=int)
    dfd_ct = pu.get_attr(dfpre, "CT", "has_defuser")
    dfd_ct = pd.DataFrame(dfd_ct,columns=['defuse_kit_ct1',\
           'defuse_kit_ct2', 'defuse_kit_ct3', 'defuse_kit_ct4', 'defuse_kit_ct5'],dtype=int)
    
    
    dfwep_t = pd.DataFrame(index=dfpre.index,columns=colwep)
    dfwep_ct = pd.DataFrame(index=dfpre.index,columns=colwep)
    dftl = pd.DataFrame(index=dfpre.index,columns=['t_leads','current_score_t',\
                                                    'current_score_ct'])
    
    
    dfwep_ct.fillna(value=0,inplace=True)
    dfwep_t.fillna(value=0,inplace=True)    
    
    dftl['current_score_t'] = dfpre['current_score'].apply(lambda x:x[1])
    dftl['current_score_ct'] = dfpre['current_score'].apply(lambda x:x[0])
    dftl['t_leads'] = dftl['current_score_t'] - dftl['current_score_ct']
    
    for i in tqdm(range(len(dfpre))):
        dft = dfpre.loc[i]
        for player in dft.alive_players:
            if player['team'] == 'CT':
                for weapon in player['inventory']:
                    if(dfwep_ct.loc[i][weapon['item_type']] is not np.nan):
                        dfwep_ct[weapon['item_type']][i] += 1
                    else:
                        dfwep_ct[weapon['item_type']][i] = 1
            else:
                for weapon in player['inventory']:
                    if(dfwep_t.loc[i][weapon['item_type']] is not np.nan):
                        dfwep_t[weapon['item_type']][i] += 1
                    else:
                        dfwep_t[weapon['item_type']][i] = 1
    dfwep_t=dfwep_t.add_suffix('_t')
    dfwep_ct=dfwep_ct.add_suffix('_ct') 
    dforg = dfpre[['map','patch_version','map_crc','round_status',\
                    'round_status_time_left','round_winner','alive_players_t',\
                    'alive_players_ct','health_t','health_ct','armor_t',\
                    'armor_ct','money_t','money_ct']]
    dforg = pu.binary_features(dfpre,all_maps,all_round_status)
    # output = pd.concat([dforg,dftl,dfwep_t,dfwep_ct,dfpla,dfbs,dfpr],axis='columns')
    output = pd.concat([dfh_t,dfh_ct,dfhh_t,dfhh_ct,dfm_t,dfm_ct,dfa_t,dfa_ct,\
                        dfwep_t,dfwep_ct,dforg,dfd_ct,dftl],axis='columns')
    
    # output.fillna(value=0,inplace=True)
    output = finalize(output)
    
    return output


    
    
                
    