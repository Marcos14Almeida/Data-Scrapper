# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:01:11 2022

@author: marcos
"""
#HOW TO USE BEAUTIFUL SOUP
#https://beautiful-soup-4.readthedocs.io/en/latest/]

import requests
from bs4 import BeautifulSoup

from save_file import saveToFile

def appendList(variable):
 lista = []
 for x in variable:
  lista.append(x.text.strip())   
 return lista   

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
#limpa os dados anteriores do arquivo
with open('people1.csv', 'w', encoding="utf-8") as csvFile:
 csvFile.close()
 

def soFifa(siteUrl):
  response = requests.get(siteUrl, headers=headers)
  html_icerigi = response.text
  soup = BeautifulSoup(html_icerigi, "html.parser")    
     
  #Attributes in HTML Code in the page   
  name = soup.find_all("a",{"role":"tooltip"})
  idade = soup.find_all("td",{"class":"col col-ae"}) 
  overall = soup.find_all("td",{"class":"col col-oa"}) 
  #pot = soup.find_all("td",{"class":"col col-pt"})  #Potencial máximo dos jogadores
  position = soup.find_all("td",{"class":"col-name"})
  
  name_list = appendList(name)
  age_list = appendList(idade)
  overall_list = appendList(overall)
  position_temporario = appendList(position)
  
  position_list = []
  for x in range (0,len(position_temporario)-1):
      if(x % 2==0):
       position_list.append(position_temporario[x])
       
  #REMOVE EMPTY VALUES FROM LIST
  name_list[:] = [x for x in name_list if x]

  for x in range (0,len(position_list)):
      if position_list[x].find(name_list[x]) != -1:
       position_list[x] = position_list[x].replace(name_list[x],'').strip()
  
  #SHOW RESULTS
  print('\nSiteUrl: '+siteUrl)
  print('NÚMERO DE JOGADORES: '+str(len(name_list)))       
  for x in range(0,len(name_list)):
     print(name_list[x],position_list[x],age_list[x],overall_list[x])   
    
  #SAVE TO CSV
  saveToFile('joao',name_list,age_list,overall_list,position_list)   