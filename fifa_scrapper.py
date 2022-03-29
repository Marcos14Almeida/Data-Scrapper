#HOW TO USE BEAUTIFUL SOUP
#https://beautiful-soup-4.readthedocs.io/en/latest/]

import file_names
from save_file import saveToFile
from global_file import globalErrors

#%%
i = 0
def showCarregando():
 global i 
 i += 1
 print('--------------------%s/16---------------------' %i)
 print('-------------------- %s%% --------------------' %round((100*i/16)))
    
 
#%%
#EUROPA
listAll = file_names.Inglaterra()
saveToFile("inglaterra",listAll)
showCarregando()

#%%
listAll = file_names.Inglaterra2()
saveToFile("inglaterra2",listAll)
showCarregando()

listAll = file_names.Espanha()
saveToFile("espanha",listAll)
showCarregando()

listAll = file_names.Italia()
saveToFile("italia",listAll)
showCarregando()

listAll = file_names.Alemanha()
saveToFile("alemanha",listAll)
showCarregando()

listAll = file_names.França()
saveToFile("franca",listAll)
showCarregando()

listAll = file_names.PTHolanda()
saveToFile("europa",listAll)
showCarregando()

listAll = file_names.LesteEuropeu()
saveToFile("leste",listAll)
showCarregando()

#AMERICA DO SUL
listAll = file_names.Brasil()
saveToFile("brasil",listAll)
showCarregando()

listAll = file_names.Brasil2()
saveToFile("brasil2",listAll)
showCarregando()

listAll = file_names.Argentina()
saveToFile("argentina",listAll)
showCarregando()

listAll = file_names.SulAmericano()
saveToFile("sulamericano",listAll)
showCarregando()

listAll = file_names.ColombiaMexico()
saveToFile("colombia",listAll)
showCarregando()


#RESTO DO MUNDO
listAll = file_names.MLS()
saveToFile("eua",listAll)
showCarregando()

listAll = file_names.Asia()
saveToFile("asia",listAll)
showCarregando()

listAll = file_names.Outros()
saveToFile("outros",listAll)


print('\nPROBLEMAS DE IMPORTAÇÃO:')
for errors in globalErrors:
 print(errors)