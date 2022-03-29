# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 23:37:06 2022

@author: marcos
"""

def renameClubs(clubName):
    
#%%     
    if(clubName == "West Ham United"):
        clubName = "West Ham"   
    elif(clubName == "Leicester City"):
        clubName = "Leicester"     
#%%
    elif(clubName == "FC Barcelona"):
        clubName = "Barcelona"
    elif(clubName == "Real Madrid CF"):
        clubName = "Real Madrid"
    elif(clubName == "Sevilla FC"):
        clubName = "Sevilla"
    elif(clubName == "Real Betis Balompié"):
        clubName = "Real Betis"
    elif(clubName == "Villarreal CF"):
        clubName = "Villarreal"
    elif(clubName == "Valencia CF"):
        clubName = "Valencia"
    elif(clubName == "Athletic Club de Bilbao"):
        clubName = "Athletic Bilbao"
        
#%%  
    elif(clubName == "AC Milan"):
        clubName = "Milan"   
  
    return clubName