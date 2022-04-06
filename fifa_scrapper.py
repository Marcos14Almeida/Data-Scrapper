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

listAll = file_names.PTHolanda()
saveToFile("pt_hol",listAll)
showCarregando()

listAll = file_names.EuropaOcidental()
saveToFile("europa_ocidental",listAll)

listAll = file_names.LesteEuropeu()
saveToFile("leste",listAll)
showCarregando()

listAll = file_names.OutrosEuropa()
saveToFile("outros_europa",listAll)

listAll = file_names.OutrosEuropa2()
saveToFile("outros_europa2",listAll)
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
#%%
listAll = file_names.SulAmericano()
saveToFile("sulamericano",listAll)
showCarregando()

listAll = file_names.Colombia()
saveToFile("colombia",listAll)
showCarregando()

listAll = file_names.OutrosAmericaSul()
saveToFile("outros_america",listAll)

#%%
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

listAll = file_names.Asia2()
saveToFile("asia2",listAll)

listAll = file_names.Africa()
saveToFile("africa",listAll)


#%%

if(len(globalErrors)>0):
 print('\nPROBLEMAS DE IMPORTAÇÃO:')
 for errors in globalErrors:
    print(errors)
    
    
#%%    
import pandas as pd
#CHECK DATASET
fileNames = ['inglaterra','inglaterra2','inglaterra3','italia','italia2',
             'espanha','espanha2','franca','franca2','alemanha','alemanha2',
             'pt_hol','europa_ocidental','leste','outros_europa','outros_europa2',
             'brasil','brasil2','brasil3','brasil4',
             'argentina','sulamericano','outros_america','colombia',
             'mexico','eua','eua2',
             'asia','asia2','africa']
dataframes = {}
for filename in fileNames:
 dataframes[filename] = pd.read_csv("data/%s.csv" %filename,header=None)    