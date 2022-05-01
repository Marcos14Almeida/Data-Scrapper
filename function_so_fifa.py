# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:01:11 2022

@author: marcos
"""
#HOW TO USE BEAUTIFUL SOUP
#https://beautiful-soup-4.readthedocs.io/en/latest/]

import requests
from bs4 import BeautifulSoup
from renameNationality import renameNationality
from class_player import Player

def appendList(variable):
 lista = []
 for x in variable:
  lista.append(x.text.strip())   
 return lista   


def soFifa(siteUrl):
    
  headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
  response = requests.get(siteUrl, headers=headers)
  soup = BeautifulSoup(response.text, "html.parser") 
     
  #Attributes in HTML Code in the page   
  name = soup.find_all("a",{"role":"tooltip"})
  idade = soup.find_all("td",{"class":"col col-ae"}) 
  overall = soup.find_all("td",{"class":"col col-oa"}) 
  #pot = soup.find_all("td",{"class":"col col-pt"})  #Potencial máximo dos jogadores
  position = soup.find_all("td",{"class":"col-name"})
  club = soup.find_all("div",{"class":"info"})
  nationalitySoup = soup.find_all('img', attrs={'class': 'flag'})  
  imageUrlSoup = soup.find_all('img', attrs={'class': 'player-check'})
  
  nationalities = getNationality(nationalitySoup)
  imageUrls = getPlayerImageUrl(imageUrlSoup)  
  

  #transform html content to a list
  name_list = appendList(name)
  age_list = appendList(idade)
  overall_list = appendList(overall)
  position_list = appendList(position)
  clubName = appendList(club)
       
  #REMOVE EMPTY NAMES FROM LIST
  name_list[:] = [x for x in name_list if x]
  
  #['Liverpool\n English Premier League (1)'] - > "Liverpool"
  clubName = clubName[0].split('\n')[0]

  positions_list = getPositionList(position_list,name_list)
           
  #SAVE DATA TO CLASS
  listAllPlayers = []
  for x in range(0,len(name_list)):
     #print(name_list[x], imageUrls[x])
     player = Player(x,clubName,name_list[x],positions_list[x],age_list[x],overall_list[x],nationalities[x],imageUrls[x])
     listAllPlayers.append(player)
  return listAllPlayers   














#%%
def getPositionList(position_temporario, name_list):
    #Weverton \nGOL \nDudu \nATA => Weverton \nDudu
    positions_list = []
    for x in range (0,len(position_temporario)-1):
        if(x % 2==0):
         positions_list.append(position_temporario[x])
         
    #TRANSFORM POSITIONS TO A STRING
    #'Lucas ATA MEI' -> replace ->' ATA MEI' -> strip -> 'ATA MEI' 
    for x in range (0,len(positions_list)):
        if positions_list[x].find(name_list[x]) != -1: #Se contem o nome do jogador
         positions_list[x] = positions_list[x].replace(name_list[x],'').strip()
         #Separate each position and change to desired name
         positions = positions_list[x].split(' ')
         string = ''
         for position in positions:
             string += updatePosition(position)+" "
         positions_list[x] = string.strip()  #remove space from the end 
         
    return positions_list
#%%
def getPlayerImageUrl(imageUrlSoup):
    #Ex Url:
    #https://cdn.sofifa.net/players/258/108/22_60.png
    imageUrls = []    
    for imageUrlHTML in imageUrlSoup:
          imageStr = str(imageUrlHTML)
          #Pega a string entre esse intervalo
          imageStr = imageStr[imageStr.find('data-src="https://cdn.sofifa.net/players'):imageStr.find('\" data-srcset')]
          imageStr = imageStr[imageStr.find('players/'):]
          imageStr = imageStr[imageStr.find('/'):]
          imageUrls.append(imageStr)
    return imageUrls
    
#%%
def getNationality(nationalitySoup):
    #GET NATIONALITY
    nationalities = []    
    for imageCountryHTML in nationalitySoup:
          imageCountryStr = str(imageCountryHTML)
          imageCountryStr = imageCountryStr[imageCountryStr.find('title='):imageCountryStr.find('\" width')]
          imageCountryStr = imageCountryStr[imageCountryStr.find('\"'):]
          imageCountryStr = imageCountryStr[1:]
          imageCountryStr = renameNationality(imageCountryStr) #To English format
          nationalities.append(imageCountryStr)
          #A lista pega de uma 2 tabelas, entao quando aparece o espaço retiramos a tabela superior
          #Ficando só com as imagens/paises da segunda tabela
          if(imageCountryStr == ""):
              nationalities = []
    return nationalities         
#%%
def updatePosition(positionName):
       if(positionName == "GK"): positionName = "GOL"
       if(positionName == "CB"): positionName = "ZAG"
       if(positionName == "RB"): positionName = "LD"
       if(positionName == "RWB"): positionName = "LD"
       if(positionName == "LWB"): positionName = "LE"
       if(positionName == "LB"): positionName = "LE"
       if(positionName == "CDM"): positionName = "VOL"
       if(positionName == "ME"): positionName = "LM"
       if(positionName == "CM"): positionName = "MC"
       if(positionName == "RM"): positionName = "MD"
       if(positionName == "LM"): positionName = "ME" 
       if(positionName == "CAM"): positionName = "MEI"
       if(positionName == "RW"): positionName = "PD"
       if(positionName == "LW"): positionName = "PE"
       if(positionName == "CF"): positionName = "ATA"       
       if(positionName == "ST"): positionName = "ATA"
       return positionName
#%%
#soFifa("https://sofifa.com/team/9/liverpool/")    
#soFifa("https://sofifa.com/team/111326/liverpool-futbol-club/")