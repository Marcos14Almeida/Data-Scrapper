# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:47:46 2022

@author: marcos
"""
import requests
import re #regular expressions
from bs4 import BeautifulSoup

#%%  
headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
#limpa os dados anteriores do arquivo
with open('people1.csv', 'w', encoding="utf-8") as csvFile:
 csvFile.close()
 
 #%%  
def soccerWiki(clubID):
    siteUrl = "https://pt-br.soccerwiki.org/squad.php?clubid="+str(clubID)
    response = requests.get(siteUrl, headers=headers)
    html_icerigi = response.text
    soup = BeautifulSoup(html_icerigi, "html.parser")    
    
#%%  
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
    overall = []
    age = []
    for x in range(0,len(all_players)):       
      #separa overall e idade e tira da linha com o jogador   
      overall.append(int(str(all_players[x][-2]+all_players[x][-1]))-7)
      age.append(all_players[x][-4]+all_players[x][-3])
      all_players[x] = all_players[x][:-4]
     
      #Retira o numero na frente do nome com o numero do uniforme
      all_players[x] = all_players[x].replace(all_players[x][0],'')
      if(all_players[x][1].isnumeric()):
        all_players[x] = all_players[x].replace(all_players[x][1],'')
      if(all_players[x][0].isnumeric()):
        all_players[x] = all_players[x].replace(all_players[x][0],'')
      #Retira certas letras indesejadas  
      all_players[x] = all_players[x].replace('ć','c')
      all_players[x] = all_players[x].replace('é','e')
      all_players[x] = all_players[x].replace('š','s')
     
#%%        
    #Ex: WeventonG -> 'Weverto','nG,'' -> 'Weverton','G'    
    names = []
    positions_list=[]
    for x in all_players:    
     positions = x.split(',')     
     name = re.split('([a-z][A-Z])',positions[0]) #() mantem os delimitadores 
     name[0] = name[0] +name[1][0] #junta o nome com a ultima letra que foi separada
     name[1] = name[1][1]+name[2] #junta o nome da posicao
     name = list(filter(None, name)) #remove espaçoes vazio
     names.append(name[0])
     positions.pop(0)
     positions.append(name[1])
     positions_list.append(positions)
     
#%%       
    #PRINT RESULT
    #print(all_players)
    print('\nSiteUrl: '+siteUrl)
    print('NÚMERO DE JOGADORES: '+str(len(all_players))) 
    for x in range(0,len(all_players)): 
     print(names[x], positions_list[x], age[x], overall[x])
     
soccerWiki(305)        