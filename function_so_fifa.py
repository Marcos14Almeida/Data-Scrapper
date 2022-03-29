# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:01:11 2022

@author: marcos
"""
#HOW TO USE BEAUTIFUL SOUP
#https://beautiful-soup-4.readthedocs.io/en/latest/]

import requests
from bs4 import BeautifulSoup

from class_player import Player

def appendList(variable):
 lista = []
 for x in variable:
  lista.append(x.text.strip())   
 return lista   


def soFifa(siteUrl):
    
  headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
  response = requests.get(siteUrl, headers=headers)
  html_icerigi = response.text
  soup = BeautifulSoup(html_icerigi, "html.parser")    
     
  #Attributes in HTML Code in the page   
  name = soup.find_all("a",{"role":"tooltip"})
  idade = soup.find_all("td",{"class":"col col-ae"}) 
  overall = soup.find_all("td",{"class":"col col-oa"}) 
  #pot = soup.find_all("td",{"class":"col col-pt"})  #Potencial máximo dos jogadores
  position = soup.find_all("td",{"class":"col-name"})
  club = soup.find_all("div",{"class":"info"})
  
  #transform html content to a list
  name_list = appendList(name)
  age_list = appendList(idade)
  overall_list = appendList(overall)
  position_temporario = appendList(position)
  clubName = appendList(club)
  clubName = clubName[0].split('\n')[0]
  
  #Weverton \nGOL \nDudu \nATA => Weverton \nDudu
  positions_list = []
  for x in range (0,len(position_temporario)-1):
      if(x % 2==0):
       positions_list.append(position_temporario[x])
       
  #REMOVE EMPTY NAMES FROM LIST
  name_list[:] = [x for x in name_list if x]

  #TRANSFORM POSITIONS TO A STRING
  #'Lucas ATA MEI' -> replace ->' ATA MEI' -> strip -> 'ATA MEI' 
  for x in range (0,len(positions_list)):
      if positions_list[x].find(name_list[x]) != -1:
       positions_list[x] = positions_list[x].replace(name_list[x],'').strip()
  
  #SHOW RESULTS
  print('\n----------------------------------------------------------------')
  print('SiteUrl: %s' %siteUrl)
  print('Time: %s' %clubName)
  print("NÚMERO DE JOGADORES: %i\n" % len(name_list)) 
  listAllPlayers = []
  for x in range(0,len(name_list)):
     player = Player(x,clubName,name_list[x],positions_list[x],age_list[x],overall_list[x])
     listAllPlayers.append(player)
     print(name_list[x],positions_list[x],age_list[x],overall_list[x])   
    
  return listAllPlayers   