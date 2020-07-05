# -*- coding: utf-8 -*-
"""
Created on Sat Jun 20 13:50:21 2020

@author: chinm
"""

from columns import colwep


def clean_weapons(df):    
    pistols=['Deagle', 'Elite', 'FiveSeven', 'Glock', 'UspS', 'Cz75Auto',\
             'R8Revolver', 'P250', 'P2000', 'Tec9','ZeusX27']
    
    smgs = ['Mp7', 'Mp9', 'Mac10', 'P90', 'Mp5sd', 'Ump45', 'Bizon']
    
    rifles = ['Ak47', 'Aug', 'Awp', 'Famas', 'G3sg1', 'GalilAr', 'M4a4',\
              'Scar20', 'Sg553', 'Ssg08', 'M4a1S']
    
    heavy = ['M249', 'Xm1014', 'Mag7', 'Negev', 'Sawedoff', 'Nova']
    
    
    main_items_t = ['Deagle','Glock','Ak47','Awp','P250','Sg553','Flashbang', \
                  'HeGrenade', 'SmokeGrenade', 'MolotovGrenade']
    
    main_items_ct = ['Deagle','Ak47','Aug','Awp','M4a4','P2000','Mp9','P250',\
                     'Sg553','UspS','Cz75Auto','Flashbang', \
                     'HeGrenade', 'SmokeGrenade', 'IncendiaryGrenade']
    
    main_items = list(set(main_items_t ) | set(main_items_ct ))
    
    other_rifles = list(map(lambda x: x if x not in main_items else None,\
                            rifles))
    while None in other_rifles:
        other_rifles.remove(None)
    other_rifles
    
    other_smgs = list(map(lambda x: x if x not in main_items else None,smgs))
    while None in other_smgs:
        other_smgs.remove(None)
    other_smgs
    
    other_heavy = heavy
    
    other_pistols = list(map(lambda x: x if x not in main_items else None,\
                             pistols))
    while None in other_pistols:
        other_pistols.remove(None)
    other_pistols
    
    main_items_t = [item+'_t' for item in main_items]
    main_items_ct = [item+'_ct' for item in main_items]
    other_rifles_t = [item+'_t' for item in other_rifles]
    other_rifles_ct = [item+'_ct' for item in other_rifles]
    other_smgs_t = [item+'_t' for item in other_smgs]
    other_smgs_ct = [item+'_ct' for item in other_smgs]
    other_pistols_t = [item+'_t' for item in other_pistols]
    other_pistols_ct = [item+'_ct' for item in other_pistols]
    other_heavy_t = [item+'_t' for item in other_heavy]
    other_heavy_ct = [item+'_ct' for item in other_heavy]
    
    
    drop_incmol = ['IncendiaryGrenade_t','MolotovGrenade_t',\
                   'IncendiaryGrenade_ct','MolotovGrenade_ct']
    drop_cols = other_rifles_t+other_rifles_ct+other_smgs_t+other_smgs_ct\
    +other_pistols_t+other_pistols_ct+other_heavy_t+other_heavy_ct\
    +drop_incmol+colwep
    df['other_rifles_t'] = df.apply(lambda x:x[other_rifles_t].sum(),axis=1)
    df['other_rifles_ct'] = df.apply(lambda x:x[other_rifles_ct].sum(),axis=1)
    
    df['other_smgs_t'] = df.apply(lambda x:x[other_smgs_t].sum(),axis=1)
    df['other_smgs_ct'] = df.apply(lambda x:x[other_smgs_ct].sum(),axis=1)
    
    df['other_heavy_t'] = df.apply(lambda x:x[other_heavy_t].sum(),axis=1)
    df['other_heavy_ct'] = df.apply(lambda x:x[other_heavy_ct].sum(),axis=1)
    
    df['other_pistols_t'] = df.apply(lambda x:x[other_pistols_t].sum(),axis=1)
    df['other_pistols_ct'] =df.apply(lambda x:x[other_pistols_ct].sum(),axis=1)
    
    df['MolotovIncendiaryGrenade_t'] = \
        df.apply(lambda x:x['IncendiaryGrenade_t']+x['MolotovGrenade_t'],\
                 axis=1)
    df['MolotovIncendiaryGrenade_ct'] = \
        df.apply(lambda x:x['IncendiaryGrenade_ct']+x['MolotovGrenade_ct'],\
                 axis=1)
    
    
    df.drop(columns=drop_cols,inplace=True)
    
    return df

def clean_kill_weapons(df):
    pistols=['Deagle', 'Elite', 'FiveSeven', 'Glock', 'UspS', 'Cz75Auto',\
             'R8Revolver', 'P250', 'P2000', 'Tec9']    
    smgs = ['Mp7', 'Mp9', 'Mac10', 'P90', 'Mp5sd', 'Ump45', 'Bizon']    
    rifles = ['Ak47', 'Aug', 'Awp', 'Famas', 'G3sg1', 'GalilAr', 'M4a4',\
              'Scar20', 'Sg553', 'Ssg08', 'M4a1S']    
    heavy = ['M249', 'Xm1014', 'Mag7', 'Negev', 'Sawedoff', 'Nova'] 
    world = ['World','Inferno']
    utils = ['DecoyGrenade','Flashbang', 'HeGrenade', 'SmokeGrenade', \
             'IncendiaryGrenade','ZeusX27']
    main_items_t = ['Deagle','Glock','Ak47','Awp','P250','Sg553','Flashbang', \
                  'HeGrenade', 'SmokeGrenade', 'MolotovGrenade']    
    main_items_ct = ['Deagle','Ak47','Aug','Awp','M4a4','P2000','Mp9','P250',\
                     'Sg553','UspS','Cz75Auto','Flashbang', \
                     'HeGrenade', 'SmokeGrenade', 'IncendiaryGrenade']
    
    main_items = list(set(main_items_t ) | set(main_items_ct ))
    
    other_rifles = list(map(lambda x: x if x not in main_items else None,\
                            rifles))
    while None in other_rifles:
        other_rifles.remove(None)
    
    other_smgs = list(map(lambda x: x if x not in main_items else None,smgs))
    while None in other_smgs:
        other_smgs.remove(None)
    
    other_heavy = heavy
    
    other_world = world
    
    other_utils = list(map(lambda x: x if x not in main_items else None,utils))
    while None in other_utils:
        other_utils.remove(None)
    
    other_pistols = list(map(lambda x: x if x not in main_items else None,\
                             pistols))
    while None in other_pistols:
        other_pistols.remove(None)
    
    main_items_t = ['kwt_'+item for item in main_items]
    main_items_ct = ['kwct_'+item for item in main_items]
    other_rifles_t = ['kwt_'+item for item in other_rifles]
    other_rifles_ct = ['kwct_'+item for item in other_rifles]
    other_smgs_t = ['kwt_'+item for item in other_smgs]
    other_smgs_ct = ['kwct_'+item for item in other_smgs]
    other_pistols_t = ['kwt_'+item for item in other_pistols]
    other_pistols_ct = ['kwct_'+item for item in other_pistols]
    other_heavy_t = ['kwt_'+item for item in other_heavy]
    other_heavy_ct = ['kwct_'+item for item in other_heavy]
    other_world_t = ['kwt_'+item for item in other_world]
    other_world_ct = ['kwct_'+item for item in other_world]
    other_utils_t = ['kwt_'+item for item in other_utils]
    other_utils_ct = ['kwct_'+item for item in other_utils]
    
    
    drop_incmol = ['kwt_IncendiaryGrenade','kwt_MolotovGrenade',\
                   'kwct_IncendiaryGrenade','kwct_MolotovGrenade']
    drop_cols = other_rifles_t+other_rifles_ct+other_smgs_t+other_smgs_ct\
    +other_pistols_t+other_pistols_ct+other_heavy_t+other_heavy_ct\
    +drop_incmol+other_world_t+other_world_ct+other_utils_t+other_utils_ct
    
    df['kwt_other_rifles'] = df.apply(lambda x:x[other_rifles_t].sum(),axis=1)
    df['kwct_other_rifles']= df.apply(lambda x:x[other_rifles_ct].sum(),axis=1)
    
    df['kwt_other_smgs'] = df.apply(lambda x:x[other_smgs_t].sum(),axis=1)
    df['kwct_other_smgs'] = df.apply(lambda x:x[other_smgs_ct].sum(),axis=1)
    
    df['kwt_other_heavy'] = df.apply(lambda x:x[other_heavy_t].sum(),axis=1)
    df['kwct_other_heavy'] = df.apply(lambda x:x[other_heavy_ct].sum(),axis=1)
    
    df['kwt_other_pistols'] = df.apply(lambda x:x[other_pistols_t].sum(),axis=1)
    df['kwct_other_pistols'] = df.apply(lambda x:x[other_pistols_ct].sum(),\
                                        axis=1)
    
    df['kwt_other_world'] = df.apply(lambda x:x[other_world_t].sum(),axis=1)
    df['kwct_other_world'] = df.apply(lambda x:x[other_world_ct].sum(),axis=1)
    
    df['kwt_other_utils'] = df.apply(lambda x:x[other_utils_t].sum(),axis=1)
    df['kwct_other_utils'] = df.apply(lambda x:x[other_utils_ct].sum(),axis=1)
    
    df['kwt_MolotovIncendiaryGrenade'] = \
        df.apply(lambda x:x['kwt_IncendiaryGrenade']+x['kwt_MolotovGrenade'],\
                 axis=1)
    df['kwct_MolotovIncendiaryGrenade'] = \
       df.apply(lambda x:x['kwct_IncendiaryGrenade']+x['kwct_MolotovGrenade'],\
                 axis=1)
    
    
    df.drop(columns=drop_cols,inplace=True)
    
    return df
