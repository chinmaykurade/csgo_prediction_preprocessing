# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 10:09:35 2020

@author: chinm
"""

import pandas as pd
import numpy as np
from tqdm import tqdm
from itertools import repeat
#from preprocess_utils import get_attr,find_in_inventory,binary_features,\
#return_pos,weapon,attacker_side,attacker_position,victim_side,victim_position\
#dist,radius_proximity,dist_pos
import preprocess_utils as pu

def position_and_Individual_stats(dfpre,colpla,colwep,colpos,all_maps,all_round_status):    
    for ds in [dfpre]:
        ds['alive_players_t']  = list(map(len ,pu.get_attr(ds, "Terrorist")))
        ds['alive_players_ct'] = list(map(len, pu.get_attr(ds, "CT")))
        ds['health_ct']        = list(map(sum, pu.get_attr(ds, "CT", "health")))
        ds['health_t']         = list(map(sum, pu.get_attr(ds, "Terrorist", "health")))
        ds['money_ct']         = list(map(sum, pu.get_attr(ds, "CT", "money")))
        ds['money_t']          = list(map(sum, pu.get_attr(ds, "Terrorist", "money")))
    
#     dfwep_t = pd.DataFrame(np.zeros((len(dfpre),len(colwep)),dtype=int),columns=colwep)
#     dfwep_ct = pd.DataFrame(np.zeros((len(dfpre),len(colwep)),dtype=int),columns=colwep)
    dfwep_t = pd.DataFrame(index=dfpre.index,columns=colwep)
    dfwep_ct = pd.DataFrame(index=dfpre.index,columns=colwep)
        
    dfpla = pd.DataFrame(index=dfpre.index,columns=colpla)
    dfpos = pd.DataFrame(index=dfpre.index,columns=colpos)
    
    players = {}  # Dictionary of list of dictionaries  
    none_list = [{},{},{},{},{},{},{},{},{},{}]
    drop = False
    drop_list = []
    curr_t_list = []
    curr_ct_list = []
    curr_t = 0
    curr_ct = 0
    for i in tqdm(range(len(dfpre))):
        dft = dfpre.loc[i]
        if(i==0 and dft['round_status']!='FreezeTime'):
            drop=True
            prev_winner = dft['round_winner']
            prev_score = dft.current_score
        num_alive = len(dft['alive_players'])
        ctc = 1
        tc = 1
        if(dft['round_status']=='FreezeTime'):
            drop = False
            if(num_alive<10):
                dfpre.drop(index=i,inplace=True)
                dfpla.drop(index=i,inplace=True)
                dfwep_t.drop(index=i,inplace=True)
                dfwep_ct.drop(index=i,inplace=True)
                dfpos.drop(index=i,inplace=True)
                drop_list.append(i)
                drop = True
                continue
            else:
                pos = [dft['alive_players'][j]['position_history'] for\
                       j in range(len(dft['alive_players']))]
                initial_pos = list(map(lambda s: s[0] if s!=[] else [],pos))
                players[i] = dft['alive_players']
                porder = []
                porder = list(map(lambda player: player['team'],players[i]))
                for j in range(10):
                    if(porder[j]=='CT'):
                        dfpla.loc[i]['health_{}{}'.format('ct',ctc)] = players[i][j]['health']
                        if(len(players[i][j]['position_history'])):
                            dfpos.loc[i]['pos_{}{}'.format('ct',ctc)] = [players[i][j]['position_history'][-1]]
                        dfpla.loc[i]['money_{}{}'.format('ct',ctc)] = players[i][j]['money']
                        dfpla.loc[i]['defuse_kit_{}{}'.format('ct',ctc)] = int(players[i][j]['has_defuser'])
                        dfpla.loc[i]['armor_{}{}'.format('ct',ctc)] = players[i][j]['armor']
                        dfpla.loc[i]['has_helmet_{}{}'.format('ct',ctc)] = int(players[i][j]['has_helmet'])
                        ctc = ctc+1
                    else:
                        dfpla.loc[i]['health_{}{}'.format('t',tc)] = players[i][j]['health']
                        if(len(players[i][j]['position_history'])):
                            try:
                                dfpos.loc[i]['pos_{}{}'.format('t',tc)] = [players[i][j]['position_history'][-1]]
                            except(IndexError):
                                print([players[i][j]['position_history']])
                        dfpla.loc[i]['money_{}{}'.format('t',tc)] = players[i][j]['money']
                        dfpla.loc[i]['armor_{}{}'.format('t',tc)] = players[i][j]['armor']
                        dfpla.loc[i]['has_helmet_{}{}'.format('t',tc)] = int(players[i][j]['has_helmet'])
                        tc = tc+1
                if(curr_t+curr_ct==15 and dfpre.loc[i].current_score != prev_score):
                    curr_ct = curr_t+curr_ct
                    curr_t = curr_ct-curr_t
                    curr_ct = curr_ct-curr_t
                if(dft.current_score==[0,0]):
                    curr_t = 0
                    curr_ct = 0
                    prev_score = dft.current_score
                    prev_winner = dft.round_winner
                else:
                    if(prev_winner=='CT' and dft.current_score != prev_score):
                        curr_ct = curr_ct+1
                        prev_score = dft.current_score
                        prev_winner = dft.round_winner
                    elif(dft.current_score != prev_score):
                        curr_t = curr_t+1
                        prev_score = dft.current_score
                        prev_winner = dft.round_winner
                
        else:
            players[i] = none_list.copy()
            if(not drop):
                for j in range(10):
                    players[i][j] = None
                    for k in range(num_alive):
                        if(initial_pos[j] == \
                            dft['alive_players'][k]['position_history'][0]):
                            players[i][j] = dft['alive_players'][k]
                            if(porder[j] == 'CT'):
                                dfpla.loc[i]['health_{}{}'.format('ct',ctc)] = players[i][j]['health']
                                if(len(players[i][j]['position_history'])):
                                    dfpos.loc[i]['pos_{}{}'.format('ct',ctc)] = [players[i][j]['position_history'][-1]]
                                dfpla.loc[i]['money_{}{}'.format('ct',ctc)] = players[i][j]['money']
                                dfpla.loc[i]['defuse_kit_{}{}'.format('ct',ctc)] = int(players[i][j]['has_defuser'])
                                dfpla.loc[i]['armor_{}{}'.format('ct',ctc)] = players[i][j]['armor']
                                dfpla.loc[i]['has_helmet_{}{}'.format('ct',ctc)] = int(players[i][j]['has_helmet'])
                                ctc = ctc+1
                            else:
                                dfpla.loc[i]['health_{}{}'.format('t',tc)] = players[i][j]['health']
                                if(len(players[i][j]['position_history'])):
                                    dfpos.loc[i]['pos_{}{}'.format('t',tc)] = [players[i][j]['position_history'][-1]]
                                dfpla.loc[i]['money_{}{}'.format('t',tc)] = players[i][j]['money']
                                dfpla.loc[i]['armor_{}{}'.format('t',tc)] = players[i][j]['armor']
                                dfpla.loc[i]['has_helmet_{}{}'.format('t',tc)] = int(players[i][j]['has_helmet'])
                                tc = tc+1
                                        
                    if(players[i][j]==None):
                        if(porder[j]=='CT'):
                            ctc = ctc+1
                        else:
                            tc = tc+1
            else:
                dfpre.drop(index=i,inplace=True)
                dfpla.drop(index=i,inplace=True)
                dfwep_t.drop(index=i,inplace=True)
                dfwep_ct.drop(index=i,inplace=True)
                dfpos.drop(index=i,inplace=True)
                drop_list.append(i)
                continue
        
        wlist_t = np.zeros((len(colwep),))
        wlist_ct = np.zeros((len(colwep),))
        for player in players[i]:
            if(player!=None):
                if(player['team']=='CT'):
                    wlist_ct = wlist_ct+np.array(list(map(lambda s:1 if(pu.find_in_inventory(player,s)==True) else 0,colwep)))
                else:
                    wlist_t = wlist_t+np.array(list(map(lambda s:1 if(pu.find_in_inventory(player,s)==True) else 0,colwep)))
        dfwep_t.loc[i] = wlist_t
        dfwep_ct.loc[i] = wlist_ct
        curr_t_list.append(curr_t)
        curr_ct_list.append(curr_ct)
    dfpre['current_score_t'] = curr_t_list
    dfpre['current_score_ct'] = curr_ct_list
    pS = pd.Series(players)
    dfpre['players'] = pS 
    dfpre.drop(columns=['alive_players'],inplace=True)
    dfwep_t=dfwep_t.add_suffix('_t')
    dfwep_ct=dfwep_ct.add_suffix('_ct')
    
    output = pd.concat([pu.binary_features(dfpre,all_maps,all_round_status),\
                        dfwep_t,dfwep_ct,dfpla,dfpos],axis='columns')
    
    output.reset_index(inplace=True)
    
    for weapon in colwep:
        output[weapon] = output[weapon+'_t'] - output[weapon+'_ct']
    
    return output


def kills_smokes_molotovs(dfpre,colsmokes,colmolotovs,colkills):
    funclist = [pu.weapon,pu.attacker_position,pu.attacker_side,\
                pu.victim_position,pu.victim_side]
    dfsmo = pd.DataFrame(index=dfpre.index,columns=colsmokes)
    dfmol = pd.DataFrame(index=dfpre.index,columns=colmolotovs)
    dfkill = pd.DataFrame(index=dfpre.index,columns=colkills)
   
#    smokes_1_list = list(map(pu.return_pos,dfpre['active_smokes'], repeat(0)))
#    smokes_2_list = list(map(pu.return_pos,dfpre['active_smokes'], repeat(1)))
#    dfsmo[colsmokes[0]] = smokes_1_list
#    dfsmo[colsmokes[1]] = smokes_2_list
    
    for i in range(len(colsmokes)):
        smokes_list = list(map(pu.return_pos,dfpre['active_smokes'], repeat(i)))
        dfsmo[colsmokes[i]] = smokes_list
    
#    mols_1_list = list(map(pu.return_pos,dfpre['active_molotovs'], repeat(0)))
#    mols_2_list = list(map(pu.return_pos,dfpre['active_molotovs'], repeat(1)))
#    dfmol[colmolotov[0]] = mols_1_list
#    dfmol[colmolotov[1]] = mols_2_list
    for i in range(len(colmolotovs)):
        molotovs_list = list(map(pu.return_pos,dfpre['active_molotovs'], repeat(i)))
        dfmol[colmolotovs[i]] = molotovs_list
        
    for i in range(int(len(colkills)/len(funclist))):
        for j,func in enumerate(funclist):
            list1 = list(map(func,dfpre['previous_kills'], repeat(i)))
            dfkill[colkills[i*len(funclist)+j]] = list1
#     return dfpre
    return pd.concat([dfpre,dfsmo,dfmol,dfkill],axis='columns')


def proximity_players(df,radius=400):
    pr_t = [[],[],[],[],[]]
    pr_ct = [[],[],[],[],[]]
    colpr = ['pr_t1','pr_t2','pr_t3','pr_t4','pr_t5','pr_ct1','pr_ct2','pr_ct3','pr_ct4','pr_ct5']
    dfpr = pd.DataFrame(index=df.index,columns=colpr)
    for i in tqdm(range(len(df))):
        dft = df.loc[i]
        for j in range(1,6):
            pr_t[j-1].append(pu.radius_proximity('t'+str(j),dft,radius = radius))
            pr_ct[j-1].append(pu.radius_proximity('ct'+str(j),dft,radius = radius))
#             dfpr.loc[i,'pr_t'+str(j)] = radius_proximity('t'+str(j),df.loc[i],radius = 300)
#             dfpr.loc[i,'pr_ct'+str(j)] = radius_proximity('ct'+str(j),df.loc[i],radius = 300)
#             print(dfpr.loc[i,'pr_t'+str(j)],dfpr.loc[i,'pr_ct'+str(j)])
    for i in range(5):
        dfpr['pr_t'+str(i+1)] = pr_t[i]
        dfpr['pr_ct'+str(i+1)] = pr_ct[i]
    
    df = pd.concat([df,dfpr],axis=1)
    return df




def pos_bs(df,colbs,maps,colmapbs):
    mbs = pu.loc_bomb_site(df,colmapbs,maps)
    default = 5000
    dfbs = pd.DataFrame(index=df.index,columns=colbs,dtype=object)
    abs_t = [[],[],[],[],[]]
    abs_ct = [[],[],[],[],[]]
    for i in tqdm(range(len(df))):
        dft = df.loc[i]
        for mapp in maps:
            if(dft[mapp] == 1):
                cmap = mapp
        mapp = cmap.split('_')[1:][0] + '_' + cmap.split('_')[1:][1]
        posA = mbs[mapp+'_A']
        posB = mbs[mapp+'_B']
        for j in range(1,6):
            if(dft['pos_t'+str(j)]is not np.nan):
                abs_t[j-1].append(np.min([pu.dist_pos(posA,dft['pos_t'+str(j)][0]),\
                                pu.dist_pos(posB,dft['pos_t'+str(j)][0])]))
            else:
                abs_t[j-1].append(default)
            if(df.loc[i,'pos_ct'+str(j)]is not np.nan):
                abs_ct[j-1].append(np.min([pu.dist_pos(posA,dft['pos_ct'+str(j)][0]),\
                                           pu.dist_pos(posB,dft['pos_ct'+str(j)][0])]))
            else:
#                 dfbs.loc[i,'pos_bs_ct'+str(j)] = default
                abs_ct[j-1].append(default)
    for j in range(1,6):
        dfbs['pos_bs_t'+str(j)] = abs_t[j-1]
        dfbs['pos_bs_ct'+str(j)] = abs_ct[j-1]
        
    df = pd.concat([df,dfbs],axis=1)
    return df