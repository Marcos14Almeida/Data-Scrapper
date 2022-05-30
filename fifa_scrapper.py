#HOW TO USE BEAUTIFUL SOUP
#https://beautiful-soup-4.readthedocs.io/en/latest/]

import file_names
from save_file import saveToFile
from global_file import globalErrors
import time
start_time = time.time()

#
##FAZER UMA VERSÃO COM WWW.FIFAINDEX NO FUTURO

#Ao acrescentar novo time: 
#1ºAcrescentar site em "FILENAMES.PY"
#2º mudar "RENAMEClubs.py"
#Se ele tiver poucos jogadores -> adicionar EM FILENAMES.PY na função "addTeamPlayers()"

globalErrors = []

#%%
i = 0
def showCarregando():
 global i 
 i += 1
 nLeagues = 30
 print('--------------------%s/%s---------------------' %(i,nLeagues))
 print('-------------------- %s%% --------------------' %round((100*i/nLeagues)))
 print("------------------ %s seconds ------------" %round(time.time() - start_time))
    
 
#%%
#EUROPA
listAll = file_names.Inglaterra()
saveToFile("inglaterra",listAll)
showCarregando()

listAll = file_names.Inglaterra2()
saveToFile("inglaterra2",listAll)
showCarregando()

listAll = file_names.Inglaterra3()
saveToFile("inglaterra3",listAll)

listAll = file_names.Inglaterra4()
saveToFile("inglaterra4",listAll)

listAll = file_names.Espanha()
saveToFile("espanha",listAll)
showCarregando()

listAll = file_names.Espanha2()
saveToFile("espanha2",listAll)
showCarregando()

listAll = file_names.Italia()
saveToFile("italia",listAll)
showCarregando()

listAll = file_names.Italia2()
saveToFile("italia2",listAll)
showCarregando()

listAll = file_names.Italia3()
saveToFile("italia3",listAll)
showCarregando()
#%%
listAll = file_names.Alemanha()
saveToFile("alemanha",listAll)
showCarregando()

listAll = file_names.Alemanha2()
saveToFile("alemanha2",listAll)

listAll = file_names.França()
saveToFile("franca",listAll)
showCarregando()

listAll = file_names.França2()
saveToFile("franca2",listAll)
showCarregando()

listAll = file_names.Portugal()
saveToFile("portugal",listAll)
showCarregando()

listAll = file_names.HolandaBelgica()
saveToFile("holanda_belgica",listAll)
showCarregando()

listAll = file_names.EuropaOcidental()
saveToFile("europa_ocidental",listAll)

listAll = file_names.EuropaOcidental2()
saveToFile("europa_ocidental2",listAll)

listAll = file_names.Nordicos()
saveToFile("nordicos",listAll)
showCarregando()

listAll = file_names.TurquiaGrecia()
saveToFile("turquia_grecia",listAll)
showCarregando()

listAll = file_names.URSS()
saveToFile("urss",listAll)
showCarregando()

listAll = file_names.LesteEuropeu()
saveToFile("europa_leste",listAll)
showCarregando()

listAll = file_names.EuropaOutros()
saveToFile("europa_outros",listAll)
#%%
#AMERICA DO SUL
listAll = file_names.Brasil()
saveToFile("brasil",listAll)
showCarregando()

listAll = file_names.Brasil2()
saveToFile("brasil2",listAll)
showCarregando()

listAll = file_names.Brasil3()
saveToFile("brasil3",listAll)
showCarregando()

listAll = file_names.Brasil4()
saveToFile("brasil4",listAll)
showCarregando()

listAll = file_names.Argentina()
saveToFile("argentina",listAll)
showCarregando()

listAll = file_names.Argentina2()
saveToFile("argentina2",listAll)
#%%
listAll = file_names.UruguaiParaguai()
saveToFile("sulamericano",listAll)
showCarregando()

listAll = file_names.Chile()
saveToFile("chile",listAll)
#%%
listAll = file_names.PeruBolivia()
saveToFile("sulamericano2",listAll)
showCarregando()

listAll = file_names.Colombia()
saveToFile("colombia",listAll)

listAll = file_names.EquadorVenezuela()
saveToFile("merconorte",listAll)
showCarregando()

#América do Norte
listAll = file_names.Mexico()
saveToFile("mexico",listAll)
showCarregando()

listAll = file_names.MLS()
saveToFile("eua",listAll)
showCarregando()

listAll = file_names.MLS2()
saveToFile("eua2",listAll)
showCarregando()

#%%
#RESTO DO MUNDO
listAll = file_names.Asia()
saveToFile("asia",listAll)
showCarregando()

listAll = file_names.Japao()
saveToFile("japao",listAll)
showCarregando()

listAll = file_names.OrienteMedio()
saveToFile("oriente_medio",listAll)
showCarregando()

listAll = file_names.Africa()
saveToFile("africa",listAll)
showCarregando()

listAll = file_names.Oceania()
saveToFile("oceania",listAll)
showCarregando()

#%%

if(len(globalErrors)>0):
 print('\nPROBLEMAS DE IMPORTAÇÃO:')
 for errors in globalErrors:
    print(errors)
    
    
#%%    
import pandas as pd
#CHECK DATASET
fileNames = ['inglaterra','inglaterra2','inglaterra3','inglaterra4',
             'italia','italia2','italia3',
             'espanha','espanha2','franca','franca2','alemanha','alemanha2',
             'portugal','holanda_belgica','europa_ocidental','europa_ocidental2','nordicos',
             'urss','turquia_grecia','europa_leste','europa_outros',
             'brasil','brasil2','brasil3','brasil4',
             'argentina','argentina2','sulamericano','chile','sulamericano2','colombia','merconorte',
             'mexico','eua','eua2',
             'asia','japao','oriente_medio','africa','oceania']
dataframes = {}
for filename in fileNames:
 dataframes[filename] = pd.read_csv("data/%s.csv" %filename,header=None)    