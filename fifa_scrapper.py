#HOW TO USE BEAUTIFUL SOUP
#https://beautiful-soup-4.readthedocs.io/en/latest/]

from function_soccer_wiki import soccerWiki
from function_so_fifa import soFifa
from file_names import *


headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
#limpa os dados anteriores do arquivo
with open('people1.csv', 'w', encoding="utf-8") as csvFile:
 csvFile.close()

    
#INICIO 
for y in range(1,9):
 url = fileNameBrasil(y)
 soccerWiki(url)
 
 url = fileNameInglaterra(y)
 soFifa(url)
 
 url = fileNameEspanha(y)
 soFifa(url)
 
 url = fileNameItalia(y)
 soFifa(url)

#End of loop