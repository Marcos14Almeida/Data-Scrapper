# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 11:05:46 2022

@author: marcos
"""
from function_soccer_wiki import soccerWiki
from function_so_fifa import soFifa
from global_file import globalErrors
from class_player import Player

##RUN FOR EACH TEAM LIST OF PLAYERS
##Retorna list of list with Player Class -> "List[Clubs][Jogador] = Player"
def getListPlayers(list):
    listAllClubsPlayers = [] 
    for indexUrl in range(0,len(list)):
        print(list[indexUrl])
        if("sofifa" in list[indexUrl]):
           listPlayers = soFifa(list[indexUrl])
        else:
           listPlayers = soccerWiki(list[indexUrl])
           
        #Se o time tem poucos jogadores, pega mais dados de outros clubes
        if(len(listPlayers)<18):  
           clubNameError = listPlayers[0].clubName
           globalErrors.append('%s - Poucos Jogadores: %s' %(clubNameError,len(listPlayers)))
           urlAdd = addTeamPlayers(clubNameError)
           additionListPlayers = soccerWiki(urlAdd)
           for players in additionListPlayers: #Muda o nome do clube pro nome do time original
               players.clubName = clubNameError
           listPlayers.extend(additionListPlayers)
           if(len(listPlayers)>15):
               globalErrors.pop() #Se continuar com o problema o globalErrors continua com a mensagem de erro
        
        #Organize players in order of Overall
        listPlayers = organizeBestPlayers(listPlayers)
        #Show RESULT
        printResult(list[indexUrl],listPlayers)
           
        listAllClubsPlayers.append(listPlayers)
        
    return listAllClubsPlayers


#%%    
def printResult(siteUrl,listPlayers):
    #PRINT RESULT    
    print('\n----------------------------------------------------------------')
    print('SiteUrl: %s' %siteUrl)
    print('Time: %s' %listPlayers[0].clubName)
    print("NÚMERO DE JOGADORES: %i\n" % len(listPlayers)) 
    for x in range(0,len(listPlayers)):
      player = listPlayers[x]        
      print(player.name,player.position,player.age,player.overall)  
    print('Time: %s' %listPlayers[0].clubName) 
    
#%%    
##SORT PLAYERS BY OVERALL
def organizeBestPlayers(listPlayers):
    
    for i in range (0,len(listPlayers)):
        for k in range (i,len(listPlayers)):
            if(listPlayers[k].overall > listPlayers[i].overall):
                aux = listPlayers[i]
                listPlayers[i] = listPlayers[k]
                listPlayers[k] = aux    
    
    return listPlayers

#%% 
#ADICIONAR JOGADORES AOS TIMES QUE TEM POUCOS JOGADORES:    
def addTeamPlayers(clubNameError):
     
    additionalUrl = ""
    
    #Place here original team name from Url Database
    if(clubNameError == 'Figueirense'):
        additionalUrl = '4764' #Sergipe
    elif(clubNameError == 'Paraná Clube'):
        additionalUrl = '2797'
    elif(clubNameError == 'Ferroviária'):
        additionalUrl = '4794' #Fluminense de Feira
    elif(clubNameError == 'São Caetano'):
        additionalUrl = '2801' #Tupi
    elif(clubNameError == 'Mirassol FC'):
        additionalUrl = '3503' #agua santa
    elif(clubNameError == 'SER Caxias do Sul'):
        additionalUrl = '3519' #guarani palhoça
    elif(clubNameError == 'Santa Cruz'):
        additionalUrl = '2394' #macaé
    elif(clubNameError == 'Botafogo PB'):
        additionalUrl = '4322' #atletico cearense
    elif(clubNameError == 'Botafogo SP'):
        additionalUrl = '5581' #floresta
    elif(clubNameError == 'Campinense Clube'):
        additionalUrl = '4758' #altos
    elif(clubNameError == 'Al Ain'):
        additionalUrl = '1346'
    elif(clubNameError == 'Al Duhail SC'):
        additionalUrl = '1213'   
    elif(clubNameError == 'Al Sadd SC'):
        additionalUrl = '1408'
    elif(clubNameError == 'Al Jazira'):
        additionalUrl = '1253'
    elif(clubNameError == 'Raja Casablanca'):
        additionalUrl = '1944'
    elif(clubNameError == 'Persepolis'):
        additionalUrl = '1394'
    elif(clubNameError == 'FC Krasnodar'):
        additionalUrl = '5535' #Veles Moskva
    elif(clubNameError == 'Manaus FC'):
        additionalUrl = '2216' #aguia maraba
    elif(clubNameError == 'FK Vardar'):
        additionalUrl = '4846' #Skopje  
    elif(clubNameError == 'TP Mazembe'):
        additionalUrl = '3208' #AS Vita    
    elif(clubNameError == 'Espérance de Tunis'):
        additionalUrl = '567' #Club Africain    
    elif(clubNameError == 'Wydad AC'):
        additionalUrl = '3942' #MC Oujda   
    elif(clubNameError == 'Al Wahda'):
        additionalUrl = '1432' #Ajman Club
    elif(clubNameError == 'FC Astana'):
        additionalUrl = '2192' #FC Kaisar
    elif(clubNameError == 'BATE'):
        additionalUrl = '1106' #Neman Grodno
    elif(clubNameError == '1º de Agosto'):
        additionalUrl = '1503' #Petro Atlético
        
    else:
        raise ValueError('Time Sem Jogadores Suficientes: '+ clubNameError)        
        
    return additionalUrl # tem que passar o parametro como lista pra funcao getListPlayers
