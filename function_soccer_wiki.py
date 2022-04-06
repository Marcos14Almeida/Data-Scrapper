# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:47:46 2022

@author: marcos
"""
import requests
import re #regular expressions
from bs4 import BeautifulSoup
from class_player import Player
 
#%%  
def soccerWiki(clubID):
    siteUrl = "https://pt-br.soccerwiki.org/squad.php?clubid="+str(clubID)
    headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
    response = requests.get(siteUrl, headers=headers)
    soup = BeautifulSoup(response.text, "html.parser")    
    
#%%  
    #Get Club Name
    soupInfos = soup.find_all("h1",{'h1','h5 heading-component-title'})
    clubName = []
    for x in soupInfos:
        clubName.append(x.text) 
    clubName = clubName[0]
    
    #Get Table Info
    soupInfos = soup.find_all("tr")
    all_table_list = [] 
    for x in soupInfos:
        all_table_list.append(x.text) 
    all_table_list.pop(0)
    
#%%  
    #A lista vem com varias linhas e campos desnesseraios como jogadores emprestados a outros clubes
    #Filtra a lista pra deixar só os jogadores
    all_players = []
    for x in all_table_list:
        if(x[0].isnumeric()):
         all_players.append(x)
        else:
            break
        
#%%          
    overall_list = []
    age_list = []
    for x in range(0,len(all_players)):       
      #separa overall e idade e tira da linha com o jogador   
      overall_list.append(int(str(all_players[x][-2]+all_players[x][-1]))-8)
      age_list.append(all_players[x][-4]+all_players[x][-3])
      all_players[x] = all_players[x][:-4]
     
      #Retira o numero na frente do nome com o numero do uniforme
      all_players[x] = all_players[x].replace(all_players[x][0],'')
      if(all_players[x][1].isnumeric()):
        all_players[x] = all_players[x].replace(all_players[x][1],'')
      if(all_players[x][0].isnumeric()):
        all_players[x] = all_players[x].replace(all_players[x][0],'')
      #Retira certas letras indesejadas  
      all_players[x] = all_players[x].replace('é','e')
      all_players[x] = all_players[x].replace('ó','o')
      all_players[x] = all_players[x].replace('ô','o')
      all_players[x] = all_players[x].replace('ã','a')
      all_players[x] = all_players[x].replace('ă','a')
      all_players[x] = all_players[x].replace('á','a')
      all_players[x] = all_players[x].replace('è','e')
      all_players[x] = all_players[x].replace('ê','e')
      all_players[x] = all_players[x].replace('í','i')
      all_players[x] = all_players[x].replace('ú','u')
      all_players[x] = all_players[x].replace('ü','u')
      all_players[x] = all_players[x].replace('ç','c')
      all_players[x] = all_players[x].replace('č','c')
      all_players[x] = all_players[x].replace('č','c')
      all_players[x] = all_players[x].replace('ć','c')
      all_players[x] = all_players[x].replace('š','s')
      all_players[x] = all_players[x].replace('ů','u')
      all_players[x] = all_players[x].replace('ý','y')
     
#%%        
    #Ex: WeventonG -> 'Weverto','nG,'' -> 'Weverton','G'    
    name_list = []
    positions_list=[]
    for x in all_players:    
      positions = x.split(',')     
      name = re.split('([a-z][A-Z])',positions[0]) #() mantem os delimitadores
      #print(name)
      name[0] = name[0] +name[1][0] #junta o nome com a ultima letra que foi separada -> Se der Erro aqui é por causa de caracter invalido
      name[1] = name[1][1]+name[2] #junta o nome da posicao
      name = list(filter(None, name)) #remove espaçoes vazio
      name_list.append(name[0])
      positions.pop(0)
      positions.append(name[1])
      positions_list.append(positions)
      
    #transforma list of positions to 1 string
    for rowNumber in range(0,len(positions_list)):
      string = ''   
      for x in range(0,len(positions_list[rowNumber])):
       positionName = positions_list[rowNumber][x]
       positionName = updatePosition(positionName) #Função para atualizar posição desejada
       string += positionName
       string += ' '
      positions_list[rowNumber] = string.strip() # remove spaces at the end   
         
    
    listAllPlayers = []
    for x in range(0,len(name_list)): 
       player = Player(x,clubName,name_list[x],positions_list[x],age_list[x],overall_list[x])
       listAllPlayers.append(player)
 
    #TODO: SORT PLAYERS
    return listAllPlayers 
 
    
 
#%%    
def updatePosition(positionName):
       if(positionName == "G"): positionName = "GOL"
       if(positionName == "D"): positionName = "ZAG"
       if(positionName == "D(C)"): positionName = "ZAG"
       if(positionName == "D(DC)"): positionName = "ZAG"
       if(positionName == "D(E)"): positionName = "LE"
       if(positionName == "D(DE)"): positionName = "LE"
       if(positionName == "D(DEC)"): positionName = "ZAG"
       if(positionName == "D(EC)"): positionName = "LE"
       if(positionName == "MD(E)"): positionName = "LE"
       if(positionName == "D(D)"): positionName = "LD"
       if(positionName == "MD(D)"): positionName = "LD"
       if(positionName == "MD(DC)"): positionName = "LD"
       if(positionName == "MD(EC)"): positionName = "MD"
       if(positionName == "MD(DE)"): positionName = "MD"
       if(positionName == "MD(C)"): positionName = "VOL"
       if(positionName == "M(E)"): positionName = "ME"
       if(positionName == "M(EC)"): positionName = "ME"
       if(positionName == "MD"): positionName = "MD"
       if(positionName == "M(DC)"): positionName = "MC"
       if(positionName == "M(C)"): positionName = "MC"
       if(positionName == "M(D)"): positionName = "MC"
       if(positionName == "M(DE)"): positionName = "MD"
       if(positionName == "M(DEC)"): positionName = "MEI"
       if(positionName == "M"): positionName = "MC"
       if(positionName == "MA(DE)"): positionName = "MEI"
       if(positionName == "MA(DEC)"): positionName = "MEI"
       if(positionName == "MA(DC)"): positionName = "MEI"
       if(positionName == "MA(C)"): positionName = "MEI"
       if(positionName == "MA(EC)"): positionName = "MEI"
       if(positionName == "MA(D)"): positionName = "PD"
       if(positionName == "MA(E)"): positionName = "PE"
       if(positionName == "MA"): positionName = "ATA"
       if(positionName == "A(C)"): positionName = "ATA"
       if(positionName == "A(DEC)"): positionName = "ATA"
       if(positionName == "A(DE)"): positionName = "PE"
       if(positionName == "A(EC)"): positionName = "PE"
       if(positionName == "A(DC)"): positionName = "ATA"
       if(positionName == "A(D)"): positionName = "PD"
       if(positionName == "A(E)"): positionName = "PE"
       
       return positionName