# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 09:57:44 2020

@author: chinm
"""

import pandas as pd
import numpy as np

def get_attr(ds, team, attr=None):
        team_players = map(lambda players: filter(lambda p: p["team"] ==\
                                                  team, players), \
                           ds['alive_players'])
        if attr:
            team_players = map(lambda players:map(lambda p: p[attr], players),\
                               team_players)
    
        return list(map(lambda p: list(p), team_players))

def find_in_inventory(player,item):
    for obj in player['inventory']:
        if(obj['item_type']==item):
            return True
    return False

def binary_features(X,all_maps,all_round_status):
    output = pd.DataFrame(index = X.index)
    # Investigate each feature column for the data
    for col, col_data in X.iteritems():
        # If data type is categorical, convert to dummy variables
        if (col=='map' or col == 'round_status'):
            col_data = pd.get_dummies(col_data, prefix = col)           
        # Collect the revised columns
        output = output.join(col_data)
    for mapp in all_maps+all_round_status:
        if(mapp not in output.columns):
            output[mapp] = np.zeros((len(output)))
    return output

def return_pos(s,idx):
    if(s!=None and s!=[]):
        if(len(s)>=idx+1):
            return s[idx]['position']
def weapon(s,idx):
    if(s!=None and s!=[]):
        if(len(s)>=idx+1):
            return s[len(s)-1-idx]['weapon']        
def attacker_side(s,idx):
    if(s!=None and s!=[]):
        if(len(s)>=idx+1):
            return s[len(s)-1-idx]['attacker_side']
def attacker_position(s,idx):
    if(s!=None and s!=[]):
        if(len(s)>=idx+1):
            return s[len(s)-1-idx]['attacker_position']
def victim_side(s,idx):
    if(s!=None and s!=[]):
        if(len(s)>=idx+1):
            return s[len(s)-1-idx]['victim_side']        
def victim_position(s,idx):
    if(s!=None and s!=[]):
        if(len(s)>=idx+1):
            return s[len(s)-1-idx]['victim_position']
        
def dist(player1,player2,df):
    param = 1500
    if(df['pos_'+player1] is np.nan):
        return 5000
    if(df['pos_'+player2] is np.nan):
        d = 5000
    else:
        d = ((df['pos_'+player1][0]['x']-df['pos_'+player2][0]['x'])**2 + \
             (df['pos_'+player1][0]['y']-df['pos_'+player2][0]['y'])**2 + \
             (df['pos_'+player1][0]['z']-df['pos_'+player2][0]['z'])**2)**(0.5)
    d = np.min([param,d])
    return d  

def radius_proximity(player,df,radius=700):
    team = player[0:-1]
    enemy = 'ct' if team == 't' else 't'
    prox = 0
    for i in range(1,6):
        d = dist(player,team+str(i),df)
        prox += 1 if d<radius else 0
        d1 = dist(player,enemy+str(i),df)
        prox -= 1 if d1<radius else 0
    return prox

def dist_pos(pos1,pos2):
    xd = pos1['x']-pos2['x']
    yd = pos1['y']-pos2['y']
    zd = pos1['z']-pos2['z']
    dist = (xd**2+yd**2+zd**2)**(0.5)
    return dist

def loc_bomb_site(df,colbs,maps): 
    mbs = {}
    for mapp in colbs:
        mbs[mapp] = {'x':0,'y':0,'z':0}
#     dfbs = pd.DataFrame(index=df.index,columns=colbs,dtype=object)
    for i in range(len(df)):
        if(df.loc[i,'planted_bomb']!=None):
            for mapp in maps:
                if(df.loc[i,mapp] == 1):
                    cmap = mapp
            mapp = cmap.split('_')[1:][0] + '_' + cmap.split('_')[1:][1]
#             print(mapp+'_'+df.loc[i,'planted_bomb']['site'])
#             print(df.loc[i,'planted_bomb']['position'])
            pos = df.loc[i,'planted_bomb']['position']
#             dfbs.loc[i,mapp+'_'+df.loc[i,'planted_bomb']['site']] = \
#             [df.loc[i,'planted_bomb']['position']]
            mbs[mapp+'_'+df.loc[i,'planted_bomb']['site']]['x'] = \
            (mbs[mapp+'_'+df.loc[i,'planted_bomb']['site']]['x'] + pos['x'])/2
            mbs[mapp+'_'+df.loc[i,'planted_bomb']['site']]['y'] = \
            (mbs[mapp+'_'+df.loc[i,'planted_bomb']['site']]['y'] + pos['y'])/2
            mbs[mapp+'_'+df.loc[i,'planted_bomb']['site']]['z'] = \
            (mbs[mapp+'_'+df.loc[i,'planted_bomb']['site']]['z'] + pos['z'])/2
    return mbs