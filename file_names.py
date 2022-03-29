# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:09:17 2022

@author: marcos
"""
from function_soccer_wiki import soccerWiki
from function_so_fifa import soFifa


##RUN FOR EACH TEAM LIST OF PLAYERS
##Retorna list of list with Player Class -> "List[Clubs][Jogador] = Player"
def runSofifa(list):
    listAllClubsPlayers = [] 
    for url in range(0,len(list)):
        listPlayers = soFifa(list[url])
        listAllClubsPlayers.append(listPlayers)
    return listAllClubsPlayers
    
def runSoccerWiki(list):
    listAllClubsPlayers = [] 
    for url in range(0,len(list)):
        listPlayers = soccerWiki(list[url])
        listAllClubsPlayers.append(listPlayers)
    return listAllClubsPlayers  




#%%
def fileNameInglaterra():    
    list = [
        "https://sofifa.com/team/5/chelsea/" ,
        "https://sofifa.com/team/10/manchester-city/" ,
        "https://sofifa.com/team/11/manchester-united/",
        "https://sofifa.com/team/1/arsenal/" ,
        "https://sofifa.com/team/9/liverpool/"  ,
        "https://sofifa.com/team/19/west-ham-united/",
        "https://sofifa.com/team/7/everton/"  ,
        "https://sofifa.com/team/95/leicester-city/"
        ]
    
    return runSofifa(list)  

#%%
def fileNameEspanha():
    list = [
        "https://sofifa.com/team/241/fc-barcelona/" ,
        "https://sofifa.com/team/243/real-madrid/" ,
        "https://sofifa.com/team/240/atletico-madrid/",
        "https://sofifa.com/team/481/sevilla-fc/" ,
        "https://sofifa.com/team/449/real-betis/"  ,
        "https://sofifa.com/team/461/valencia-cf/",
        "https://sofifa.com/team/483/villarreal-cf/" ,
        "https://sofifa.com/team/448/athletic-club-de-bilbao/"
     ]      
    
    return runSofifa(list) 

#%%
def fileNameItalia():  
    list = [
        "https://sofifa.com/team/45/juventus/" ,
        "https://sofifa.com/team/44/inter/",
        "https://sofifa.com/team/48/napoli/"  ,
        "https://sofifa.com/team/46/lazio/",
        "https://sofifa.com/team/47/milan/",
        "https://sofifa.com/team/52/roma/",
        "https://sofifa.com/team/39/atalanta/" ,
        "https://sofifa.com/team/110374/fiorentina/",
        ]
    
    return runSofifa(list) 

#%%
def fileNameBrasil(): 
    list = [
        "300", #Palmeiras
        "300", #Palmeiras
        "300", #Palmeiras
        "300", #Palmeiras
        "300", #Palmeiras
        "300", #Palmeiras
        "300", #Palmeiras
        "300", #Palmeiras
        ]

    return runSoccerWiki(list)  
 #%%
def fileNameOutros(): 
     list = [
         "306", #Palmeiras
         "323", #Palmeiras
         "354", #Palmeiras
         "322", #Palmeiras
         "398", #Palmeiras
         "302", #Palmeiras
         "303", #Palmeiras
         "300", #Palmeiras
         ]

     return runSoccerWiki(list)         
