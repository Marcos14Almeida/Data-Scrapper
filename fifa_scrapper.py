#HOW TO USE BEAUTIFUL SOUP
#https://beautiful-soup-4.readthedocs.io/en/latest/]

from file_names import *
from save_file import saveToFile

listAll = fileNameOutros()
saveToFile("outros",listAll)

listAll = fileNameBrasil()
saveToFile("brasil",listAll)

listAll = fileNameInglaterra()
saveToFile("inglaterra",listAll)

listAll = fileNameEspanha()
saveToFile("espanha",listAll)

listAll = fileNameItalia()
saveToFile("italia",listAll)

