# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 18:02:23 2022

@author: marcos
"""

import csv

def saveToFile(filename,name_list,idade_list,overall_list,position_list):
   #SAVE TO CSV
   with open(filename+'.csv', 'a', encoding="utf-8") as csvFile:
      writer = csv.writer(csvFile)
      writer.writerow(name_list)
      writer.writerow(idade_list)
      writer.writerow(overall_list)
      writer.writerow(position_list)
   csvFile.close    
    