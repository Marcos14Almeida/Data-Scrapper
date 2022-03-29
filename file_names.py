# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 16:09:17 2022

@author: marcos
"""
from function_soccer_wiki import soccerWiki
from function_so_fifa import soFifa


##RUN FOR EACH TEAM LIST OF PLAYERS
##Retorna list of list with Player Class -> "List[Clubs][Jogador] = Player"
def getListPlayers(list):
    listAllClubsPlayers = [] 
    for url in range(0,len(list)):
        if("sofifa" in list[url]):
           listPlayers = soFifa(list[url])
        else:
           listPlayers = soccerWiki(list[url])
        listAllClubsPlayers.append(listPlayers)
    return listAllClubsPlayers
    


#%%
def Inglaterra():    
    list = [
        "https://sofifa.com/team/5/chelsea/" ,
        "https://sofifa.com/team/10/manchester-city/" ,
        "https://sofifa.com/team/11/manchester-united/",
        "https://sofifa.com/team/1/arsenal/" ,
        "https://sofifa.com/team/9/liverpool/"  ,
        "https://sofifa.com/team/18/tottenham-hotspur/",
        "https://sofifa.com/team/7/everton/"  ,
        "https://sofifa.com/team/95/leicester-city/",
        
        "https://sofifa.com/team/19/west-ham-united/",
        "https://sofifa.com/team/13/newcastle-united/",
        "https://sofifa.com/team/17/southampton/",
        "https://sofifa.com/team/2/aston-villa/",
        "https://sofifa.com/team/110/wolverhampton-wanderers/",
        "https://sofifa.com/team/1799/crystal-palace/", 
        "https://sofifa.com/team/109/west-bromwich-albion/",       
        ]
    
    return getListPlayers(list)  
#%%
def Inglaterra2():    
    list = [
        "https://sofifa.com/team/88/birmingham-city/" ,
        "https://sofifa.com/team/3/blackburn-rovers/" ,
        "https://sofifa.com/team/1796/burnley/",
        "https://sofifa.com/team/1808/brighton-hove-albion/" ,
        "https://sofifa.com/team/91/derby-county/"  ,
        "https://sofifa.com/team/144/fulham/",
        "https://sofifa.com/team/12/middlesbrough/",
        
        "https://sofifa.com/team/1943/afc-bournemouth/",
        "https://sofifa.com/team/1792/norwich-city/",
        "https://sofifa.com/team/14/nottingham-forest/",
        "https://sofifa.com/team/15/queens-park-rangers/",
        "https://sofifa.com/team/1793/reading/",
        "https://sofifa.com/team/1794/sheffield-united/",
        "https://sofifa.com/team/1806/stoke-city/", 
        "https://sofifa.com/team/1960/swansea-city/",       
        ]
    
    return getListPlayers(list) 
#%%
def Espanha():
    list = [
        "https://sofifa.com/team/241/fc-barcelona/" ,
        "https://sofifa.com/team/243/real-madrid/" ,
        "https://sofifa.com/team/240/atletico-madrid/",
        "https://sofifa.com/team/481/sevilla-fc/" ,
        "https://sofifa.com/team/449/real-betis/"  ,
        "https://sofifa.com/team/461/valencia-cf/",
        "https://sofifa.com/team/483/villarreal-cf/" ,
        "https://sofifa.com/team/448/athletic-club-de-bilbao/",
        
 
        "https://sofifa.com/team/457/real-sociedad/" ,
        "https://sofifa.com/team/1860/getafe-cf/" ,  
        "https://sofifa.com/team/450/rc-celta-de-vigo/" ,  
        "https://sofifa.com/team/452/rcd-espanyol-de-barcelona/" ,  
        "https://sofifa.com/team/1853/levante-union-deportiva/" ,  
        "https://sofifa.com/team/479/ca-osasuna/" ,    
        "https://sofifa.com/team/462/real-valladolid-cf/" ,  
        "https://sofifa.com/team/467/sd-eibar/" , #-> LA CORUNA 
     ]      
    
    return getListPlayers(list) 

#%%
def Italia():  
    list = [
        "https://sofifa.com/team/45/juventus/" ,
        "https://sofifa.com/team/44/inter/",
        "https://sofifa.com/team/48/napoli/"  ,
        "https://sofifa.com/team/46/lazio/",
        "https://sofifa.com/team/47/milan/",
        "https://sofifa.com/team/52/roma/",
        "https://sofifa.com/team/39/atalanta/" ,
        "https://sofifa.com/team/110374/fiorentina/",
        
        "https://sofifa.com/team/1837/uc-sampdoria/" ,
        "https://sofifa.com/team/54/torino-fc/" ,
        "https://sofifa.com/team/111974/us-sassuolo-calcio/" ,
        "https://sofifa.com/team/189/bologna/" ,
        "https://sofifa.com/team/55/udinese-calcio/" ,
        "https://sofifa.com/team/1842/cagliari/" ,
        "https://sofifa.com/team/110556/genoa/" ,
        "https://sofifa.com/team/50/parma/" ,
        ]
    
    return getListPlayers(list) 
#%%
def Alemanha():  
    list = [
        "https://sofifa.com/team/21/fc-bayern-munchen/" ,
        "https://sofifa.com/team/22/borussia-dortmund/",
        "https://sofifa.com/team/112172/rb-leipzig/",
        "https://sofifa.com/team/32/bayer-04-leverkusen/",
        "https://sofifa.com/team/23/borussia-monchengladbach/",
        "https://sofifa.com/team/1824/eintracht-frankfurt/",
        "https://sofifa.com/team/10029/tsg-hoffenheim/",
        "https://sofifa.com/team/175/vfl-wolfsburg/",
        
        "https://sofifa.com/team/166/hertha-bsc/",
        "https://sofifa.com/team/31/1-fc-koln/",
        "https://sofifa.com/team/36/vfb-stuttgart/",
        "https://sofifa.com/team/100409/fc-augsburg/",
        "https://sofifa.com/team/38/sv-werder-bremen/",
        "https://sofifa.com/team/28/hamburger-sv/",
        "https://sofifa.com/team/34/fc-schalke-04/",
        "https://sofifa.com/team/25/sport-club-freiburg/",
        ]
    
    return getListPlayers(list) 
#%%
def França():  
    list = [
        "https://sofifa.com/team/73/paris-saint-germain/",     
        "https://sofifa.com/team/66/olympique-lyonnais/", 
        "https://sofifa.com/team/219/olympique-de-marseille/", 
        "https://sofifa.com/team/69/as-monaco/", 
        "https://sofifa.com/team/65/losc-lille/", 
        "https://sofifa.com/team/72/ogc-nice/", 
        "https://sofifa.com/team/74/stade-rennais-fc/", 
        "https://sofifa.com/team/70/montpellier-herault-sc/", 
        
        "https://sofifa.com/team/1819/as-saint-etienne/", 
        "https://sofifa.com/team/59/fc-girondins-de-bordeaux/", 
        "https://sofifa.com/team/71/fc-nantes/", 
        "https://sofifa.com/team/379/stade-de-reims/", 
        "https://sofifa.com/team/68/fc-metz/", 
        "https://sofifa.com/team/231/club-brugge-kv/", 
        "https://sofifa.com/team/232/standard-de-liege/", 
        "https://sofifa.com/team/229/rsc-anderlecht/", 
        ]
    
    return getListPlayers(list) 
#%%
def PTHolanda(): 
    list = [
        "https://sofifa.com/team/234/sl-benfica/" ,
        "https://sofifa.com/team/237/sporting-cp/" ,
        "https://sofifa.com/team/236/fc-porto/" ,
        "https://sofifa.com/team/1896/sc-braga/" ,
        "https://sofifa.com/team/1887/vitoria-de-guimaraes/" ,
        "https://sofifa.com/team/1898/boavista-fc/" ,
        "https://sofifa.com/team/1893/clube-sport-maritimo/" ,
        "https://sofifa.com/team/10031/portimonense-sc/" ,
        
        
        "https://sofifa.com/team/245/ajax/" ,
        "https://sofifa.com/team/247/psv/" ,
        "https://sofifa.com/team/246/feyenoord/" ,
        "https://sofifa.com/team/1906/az-alkmaar/" ,
        "https://sofifa.com/team/1908/fc-twente/" ,
        "https://sofifa.com/team/1909/vitesse/" ,
        "https://sofifa.com/team/1903/fc-utrecht/" ,
        "https://sofifa.com/team/1913/sc-heerenveen/" ,
        ]
    
    return getListPlayers(list)  
#%%
def LesteEuropeu(): 
    list = [
        "265", #Zenit
        "263", #Spartak
        "254", #CSKA
        "1673", #Krasnodar
        "351", #Galatasaray
        "349", #Besiktas
        "350", #Fenerbahce
        "373", #Olympiakos
        
        "381", #Partizan
        "380", #Estrela Vermelha
        "1763", #Ludogorets
        "365", #D. Zagreb
        "348", #Shaktar
        "347", #Dinamo Kiev
        "369", #Sparta Praga
        "719", #Apoel
        ]

    return getListPlayers(list) 
###################################################
###################################################
###################################################
#%%
def Brasil(): 
    list = [
        "300", #Palmeiras
        "290", #Corinthians
        "306", #SP
        "304", #Santos
        "286", #Atl-MG
        "298", #Internacional
        "294", #Flamengo
        "288", #Botafogo
        
        "295", #Fluminense
        "287", #Atl-PR
        "291", #Coritiba
        "296", #Fortaleza
        "1458", #Ceará
        "1447", #RB Bragantino
        "1581", #Atl-GO
        "297", #Goias
        ]

    return getListPlayers(list)  
#%%
def Brasil2(): 
    list = [
        "602", #Grêmio
        "290", #América-MG
        "306", #Bahia
        "304", #Chape
        "286", #Cuiaba
        "1772", #Criciuma
        "298", #Cruzeiro
        "293", #Figueirense
        
        "1515", #Guarani
        "299", #Juventude
        "922", #Naútico
        "301", #Paraná
        "303", #Ponte Preta
        "923", #Sport
        "307", #Vasco
        "1237", #Vitória
        ]

    return getListPlayers(list)  
#%%
def Argentina():  
    list = [
        "https://sofifa.com/team/1876/river-plate/",
        "https://sofifa.com/team/1877/boca-juniors/",
        "https://sofifa.com/team/110406/club-atletico-colon/",
        "https://sofifa.com/team/101085/racing-club/",
        "https://sofifa.com/team/110093/club-atletico-independiente/",
        "https://sofifa.com/team/101088/velez-sarsfield/",
        "https://sofifa.com/team/110395/club-atletico-lanus/",
        "https://sofifa.com/team/101083/estudiantes-de-la-plata/",
        
        "https://sofifa.com/team/110580/rosario-central/",
        "https://sofifa.com/team/1013/san-lorenzo-de-almagro/",
        "https://sofifa.com/team/110396/newells-old-boys/",
        "https://sofifa.com/team/111019/argentinos-juniors/",
        "https://sofifa.com/team/112670/club-atletico-talleres/",
        "https://sofifa.com/team/110394/arsenal-de-sarandi/",
        "https://sofifa.com/team/110404/club-atletico-banfield/",
        "https://sofifa.com/team/111710/defensa-y-justicia/",
        ]
    
    return getListPlayers(list) 
#%%
def SulAmericano(): 
    list = [
        "376", #Penarol
        "375", #Nacional-URU
        "613", #Olimpia
        "615", #Cerro
        "616", #Libertad
        "362", #colo-colo
        "364", #laU
        "363", #Catolica
        
        "1238", #Bolivar
        "1562", #Del Valle
        "656", #LDU
        "886", #Emelec
        "658", #Barcelona-EQU
        "509", #Sporting Cristal
        "621", #Alianza Lima
        "1211", #Caracas
        ]

    return getListPlayers(list)
#%%
def ColombiaMexico(): 
    list = [
        "620", #América de Cali
        "912", #Atlético Nacional
        "906", #Deportivo Cali
        "853", #Junior
        "911", #DIM
        "619", #Once Caldas
        "618", #Millonarios
        "916", #Santa fé
        
        "439", #América
        "444", #Chivas
        "443", #Cruz Azul
        "445", #Monterrey
        "447", #Pachuca
        "453", #Pumas
        "450", #Tigres
        "451", #Toluca
        ]

    return getListPlayers(list)
#%%
def MLS():  
    list = [
        "https://sofifa.com/team/111144/seattle-sounders-fc/" ,
        "https://sofifa.com/team/112996/los-angeles-fc/" ,
        "https://sofifa.com/team/687/columbus-crew/" ,
        "https://sofifa.com/team/111140/portland-timbers/" ,
        "https://sofifa.com/team/691/new-england-revolution/" ,
        "https://sofifa.com/team/112828/new-york-city-fc/" ,
        "https://sofifa.com/team/112606/orlando-city-soccer-club/" ,
        "https://sofifa.com/team/112885/atlanta-united/" ,
        
        "https://sofifa.com/team/112893/inter-miami-cf/" ,
        "https://sofifa.com/team/111138/minnesota-united-fc/" ,
        "https://sofifa.com/team/695/fc-dallas/" ,
        "https://sofifa.com/team/101112/vancouver-whitecaps-fc/" ,
        "https://sofifa.com/team/689/new-york-red-bulls/" ,
        "https://sofifa.com/team/697/la-galaxy/" ,
        "https://sofifa.com/team/688/dc-united/" ,
        "https://sofifa.com/team/111651/toronto-fc/" ,
        ]
    
    return getListPlayers(list) 
#%%
def Asia(): 
    list = [
        "2288", #Shanghai
        "1521", #Ghuangzou
        "1068", #Shandong
        "517", #Urawa
        "527", #Kawasaki
        "518", #Kashima
        "1079", #Vissel Kobe
        "1059", #Pohang Steelers
        
        "680", #Jeonbuk Hyundai
        "1323", #Al-Ain
        "1252", #Al-Sadd
        "625", #Al-Hilal
        "665", #Al-Nassr
        "628", #Al-Ahli
        "1610", #Al-Duhail
        "1347", #Al-Jazira
        ]

    return getListPlayers(list)
 #%%
def Outros(): 
     list = [
         "522", #Al-Ahly
         "521", #Zamalek
         "573", #Raja Casablanca
         "1232", #Portuguesa
         "917", #Tolima
         "896", #Cienciano
         "1414", #Avaí
         "603", #Santa Cruz
         "https://sofifa.com/team/1952/hull-city/"  ,
         "685", #Persepolis
         "681", #Ulsan Hyundai
         "274", #Huracan
         ]

     return getListPlayers(list)         
