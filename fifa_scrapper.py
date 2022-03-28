#HOW TO USE BEAUTIFUL SOUP
#https://beautiful-soup-4.readthedocs.io/en/latest/]

import requests
import csv
from bs4 import BeautifulSoup
import re
 
def appendList(variable):
 lista = []
 for x in variable:
  lista.append(x.text.strip())   
 return lista   

headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}
#limpa os dados anteriores do arquivo
with open('people1.csv', 'w', encoding="utf-8") as csvFile:
 csvFile.close()
 
for y in range(1,24):
 if (y==1):
    url = "https://sofifa.com/team/5/chelsea/"
 if (y==2):    
    url = "https://sofifa.com/team/10/manchester-city/"
 if (y==3): 
    url = "https://sofifa.com/team/11/manchester-united/"
 if (y==4): 
    url = "https://sofifa.com/team/1/arsenal/"
 if (y==5): 
    url = "https://sofifa.com/team/9/liverpool/"   
 if (y==6): 
    url = "https://sofifa.com/team/19/west-ham-united/"       
 if (y==7): 
    url = "https://sofifa.com/team/7/everton/"       
 if (y==8): 
    url = "https://sofifa.com/team/95/leicester-city/"      
 if (y==9): 
    url = "https://sofifa.com/team/241/fc-barcelona/"    
 if (y==10): 
    url = "https://sofifa.com/team/243/real-madrid/" 
 if (y==11): 
    url = "https://sofifa.com/team/240/atletico-madrid/" 
 if (y==12): 
    url = "https://sofifa.com/team/481/sevilla-fc/"     
 if (y==13): 
    url = "https://sofifa.com/team/449/real-betis/"      
 if (y==14): 
    url = "https://sofifa.com/team/461/valencia-cf/"      
 if (y==15): 
    url = "https://sofifa.com/team/483/villarreal-cf/"      
 if (y==16): 
    url = "https://sofifa.com/team/448/athletic-club-de-bilbao/"     
 if (y==17): 
    url = "https://sofifa.com/team/45/juventus/"     
 if (y==18): 
    url = "https://sofifa.com/team/44/inter/"   
 if (y==19): 
    url = "https://sofifa.com/team/48/napoli/"   
 if (y==20): 
    url = "https://sofifa.com/team/46/lazio/"   
 if (y==21): 
    url = "https://sofifa.com/team/47/milan/"   
 if (y==22): 
    url = "https://sofifa.com/team/52/roma/" 
 if (y==23): 
    url = "https://sofifa.com/team/39/atalanta/" 
 if (y==24): 
    url = "https://sofifa.com/team/110374/fiorentina/" 





    
 response = requests.get(url, headers=headers)
 html_icerigi = response.text
 soup = BeautifulSoup(html_icerigi, "html.parser")    
    
 #Attributes in HTML Code in the page   
 name = soup.find_all("a",{"role":"tooltip"})
 idade = soup.find_all("td",{"class":"col col-ae"}) 
 overall = soup.find_all("td",{"class":"col col-oa"}) 
 pot = soup.find_all("td",{"class":"col col-pt"}) 
 position = soup.find_all("td",{"class":"col-name"})
 
 name_list = appendList(name)
 idade_list = appendList(idade)
 overall_list = appendList(overall)
 pot_list = appendList(pot)
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
 for x in range(0,len(name_list)):
    print(name_list[x],idade_list[x],overall_list[x],pot_list[x],position_list[x])   

  
 #SAVE TO CSV
 with open('people1.csv', 'a', encoding="utf-8") as csvFile:
    writer = csv.writer(csvFile)
    writer.writerow(name_list)
    writer.writerow(idade_list)
    writer.writerow(overall_list)
    writer.writerow(pot_list)
    writer.writerow(position_list)
 csvFile.close
 
url = "https://pt-br.soccerwiki.org/squad.php?clubid=300" 
idade = soup.find_all("td",{"title":"Goleiro"})
idade_lista = [] 
for x in idade:
    idade_lista.append(x.text.strip()) 
    
    
    
