# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 11:45:17 2022

@author: marcos
"""

import pandas as pd
league_players = pd.read_csv("data/asia.csv",header=None)



#%%
league_players.to_csv("data/asia.csv", header=None, index=False,sep=',', encoding='utf-8')