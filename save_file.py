# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 18:02:23 2022

@author: marcos
"""

import csv
from class_player import Player
from renameClubs import renameClubs


#%%
def saveToFile(filename,listAllPlayers):
    #limpa os dados anteriores do arquivo
    with open('data/'+filename+'.csv', 'w', encoding="utf-8") as csvFile:
        csvFile.close()
    
    
#%%    
    row_string = []    
    
    #ADD 1 LINHA  
    string = ""  
    for clubsIndex in range(0,len(listAllPlayers)):
          player = listAllPlayers[clubsIndex][0]
          player.clubName = renameClubs(player.clubName)
          string += player.clubName+",,,,,"  
    row_string.append(['a,'+string])
    
    #TRANSFORM LIST OF PLAYERS INTO ROWS TO SAVE IN CSV
    for playerIndex in range(0,50):      
      string = ""
      for clubsIndex in range(0,len(listAllPlayers)):
          #todo: Check if position exist
          #print(listAllPlayers[clubsIndex][playerIndex].name)
          if(len(listAllPlayers[clubsIndex]) > playerIndex):
              player = listAllPlayers[clubsIndex][playerIndex]
              string += player.name+","+player.position+","+ str(player.age)+","+ str(player.overall)+",,"
          else:
              string += ',,,,,'      
      row_string.append(['a,'+string])
        

          
#%%                
    #SAVE TO CSV
    with open('data/'+filename+'.csv', 'a', encoding="utf-8") as csvFile:
       writer = csv.writer(csvFile, quoting=csv.QUOTE_NONE, escapechar='\\') #remove quotes in the beggining and end of row
       for string in row_string:
           writer.writerow(string)
    csvFile.close    
#%%

 #Remove // character do escapechar adiconado um pouco antes
 #Alem de remover \\ ele tambem da uma quebra de linha a mais desnecessária
    text = open('data/'+filename+'.csv', "r", encoding="utf8")
    text = ''.join([i for i in text]).replace("\\", "").replace("\na", "a")
    x = open('data/'+filename+'.csv',"w", encoding="utf8")
    x.writelines(text)
    x.close()
        
