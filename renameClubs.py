# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 23:37:06 2022

@author: marcos
"""

def renameClubs(clubName):
    
#%%     
    if(clubName == "West Ham United"):
        clubName = "West Ham"   
    elif(clubName == "Leicester City"):
        clubName = "Leicester"     
    elif(clubName == "Tottenham Hotspur"):
        clubName = "Tottenham"    
    elif(clubName == "Newcastle United"):
        clubName = "Newcastle"
    elif(clubName == "Wolverhampton Wanderers"):
        clubName = "Wolves"
    elif(clubName == "West Bromwich Albion"):
        clubName = "West Bromwich" 
#%%         
    elif(clubName == "Birmingham City"):
        clubName = "Birmingham"
    elif(clubName == "Derby County"):
        clubName = "Derby County"
    elif(clubName == "Blackburn Rovers"):
        clubName = "Blackburn"        
    elif(clubName == "AFC Bournemouth"):
        clubName = "Bournemouth" 
    elif(clubName == "Brighton & Hove Albion"):
        clubName = "Brighton"    
    elif(clubName == "Norwich City"):
        clubName = "Norwich"          
    elif(clubName == "Queens Park Rangers"):
        clubName = "QPR"          
    elif(clubName == "Swansea City"):
        clubName = "Swansea"          
#%%
    elif(clubName == "FC Barcelona"):
        clubName = "Barcelona"
    elif(clubName == "Real Madrid CF"):
        clubName = "Real Madrid"
    elif(clubName == "Atlético de Madrid"):
        clubName = "Atlético Madrid"        
    elif(clubName == "Sevilla FC"):
        clubName = "Sevilla"
    elif(clubName == "Real Betis Balompié"):
        clubName = "Real Betis"
    elif(clubName == "Villarreal CF"):
        clubName = "Villarreal"
    elif(clubName == "Valencia CF"):
        clubName = "Valencia"
    elif(clubName == "Athletic Club de Bilbao"):
        clubName = "Athletic Bilbao"
    elif(clubName == "Getafe CF"):
        clubName = "Getafe"
    elif(clubName == "RC Celta de Vigo"):
        clubName = "Celta de Vigo"
    elif(clubName == "RCD Espanyol de Barcelona"):
        clubName = "Espanyol"
    elif(clubName == "Levante Unión Deportiva"):
        clubName = "Levante" 
    elif(clubName == "CA Osasuna"):
        clubName = "Osasuna"  
    elif(clubName == "Real Valladolid CF"):
        clubName = "Valladolid" 
    elif(clubName == "AD Alcorcón"):
        clubName = "La Coruna"    
#%%
    elif(clubName == "Granada CF"):
        clubName = "Granada"
    elif(clubName == "Elche CF"):
        clubName = "Elche"
    elif(clubName == "Cádiz CF"):
        clubName = "Cádiz"
    elif(clubName == "Elche CF"):
        clubName = "Elche"
    elif(clubName == "RCD Mallorca"):
        clubName = "Mallorca" 
    elif(clubName == "CD Leganés"):
        clubName = "Leganés"    
    elif(clubName == "UD Ibiza"):
        clubName = "Ibiza"    
    elif(clubName == "Málaga CF"):
        clubName = "Málaga"    
    elif(clubName == "Unión Deportiva Las Palmas"):
        clubName = "Las Palmas"    
    elif(clubName == "Unión Deportiva Almería"):
        clubName = "Almería"    
    elif(clubName == "SD Eibar"):
        clubName = "Eibar"    
    elif(clubName == "Real Sporting de Gijón"):
        clubName = "Sporting de Gijón"    
    elif(clubName == "CD Tenerife"):
        clubName = "Tenerife"            
#%%  
    elif(clubName == "AC Milan"):
        clubName = "Milan"
    elif(clubName == "U.C. Sampdoria"):
        clubName = "Sampdoria" 
    elif(clubName == "Torino F.C."):
        clubName = "Torino"
    elif(clubName == "U.S. Sassuolo Calcio"):
        clubName = "Sassuolo" 
    elif(clubName == "Udinese Calcio"):
        clubName = "Udinese"
#%%
    elif(clubName == "AC Monza"):
        clubName = "Monza"  
    elif(clubName == "Brescia Calcio"):
        clubName = "Brescia"          
    elif(clubName == "Pisa SC"):
        clubName = "Pisa"            
    elif(clubName == "AC Perugia"):
        clubName = "Perugia"          
#%%  
    elif(clubName == "Paris Saint-Germain"):
        clubName = "PSG"
    elif(clubName == "Olympique Lyonnais"):
        clubName = "Lyon"
    elif(clubName == "Olympique de Marseille"):
        clubName = "Olympique Marselha"
    elif(clubName == "AS Monaco"):
        clubName = "Monaco"
    elif(clubName == "LOSC Lille"):
        clubName = "Lille"
    elif(clubName == "OGC Nice"):
        clubName = "Nice"
    elif(clubName == "Stade Rennais FC"):
        clubName = "Rennes"
    elif(clubName == "Montpellier Hérault SC"):
        clubName = "Montpellier"
    elif(clubName == "AS Saint-Étienne"):
        clubName = "Saint-Etienne"
    elif(clubName == "FC Girondins de Bordeaux"):
        clubName = "Bordeaux"
    elif(clubName == "FC Nantes"):
        clubName = "Nantes"        
    elif(clubName == "Stade de Reims"):
        clubName = "Reims"
    elif(clubName == "FC Metz"):
        clubName = "Metz"
    elif(clubName == "Racing Club de Lens"):
        clubName = "Lens"
    elif(clubName == "RC Strasbourg Alsace"):
        clubName = "Strasbourg"         
#%%
    elif(clubName == "Clermont Foot 63"):
        clubName = "Clermont"  
    elif(clubName == "ESTAC Troyes"):
        clubName = "Troyes" 
    elif(clubName == "Angers SCO"):
        clubName = "Angers" 
    elif(clubName == "Stade Brestois 29"):
        clubName = "Stade Brestois"        
    elif(clubName == "Toulouse Football Club"):
        clubName = "Toulouse"         
    elif(clubName == "Stade Malherbe Caen"):
        clubName = "Caen"        
    elif(clubName == "AJ Auxerre"):
        clubName = "Auxerre" 
    elif(clubName == "Nîmes Olympique"):
        clubName = "Nîmes"           
    elif(clubName == "Amiens SC"):
        clubName = "Amiens"           
    elif(clubName == "Dijon FCO"):
        clubName = "Dijon"           
#%% 
    elif(clubName == "FC Bayern München"):
        clubName = "Bayern Munique"
    elif(clubName == "Bayer 04 Leverkusen"):
        clubName = "Bayer Leverkusen"        
    elif(clubName == "Borussia Mönchengladbach"):
        clubName = "Moenchengladbach"
    elif(clubName == "TSG Hoffenheim"):
        clubName = "Hoffenheim"
    elif(clubName == "VfL Wolfsburg"):
        clubName = "Wolfsburg"
    elif(clubName == "Hertha BSC"):
        clubName = "Hertha Berlim"
    elif(clubName == "1. FC Köln"):
        clubName = "Colonia"
    elif(clubName == "VfB Stuttgart"):
        clubName = "Stuttgart"
    elif(clubName == "FC Augsburg"):
        clubName = "Augsburg"
    elif(clubName == "SV Werder Bremen"):
        clubName = "Werder Bremen"
    elif(clubName == "Hamburger SV"):
        clubName = "Hamburgo" 
    elif(clubName == "FC Schalke 04"):
        clubName = "Schalke-04"
    elif(clubName == "Sport-Club Freiburg"):
        clubName = "Freiburg"
#%%
    elif(clubName == "1. FSV Mainz 05"):
        clubName = "Mainz 05"
    elif(clubName == "1. FC Union Berlin"):
        clubName = "Union Berlin"   
    elif(clubName == "DSC Arminia Bielefeld"):
        clubName = "Arminia Bielefeld"     
    elif(clubName == "VfL Bochum 1848"):
        clubName = "Bochum 1848"
    elif(clubName == "1. FC Nürnberg"):
        clubName = "Nurnberg"            
    elif(clubName == "FC St. Pauli"):
        clubName = "St. Pauli"  
    elif(clubName == "1. FC Kaiserslautern"):
        clubName = "Kaiserslautern"  
    elif(clubName == "SG Dynamo Dresden"):
        clubName = "Dynamo Dresden"            
    elif(clubName == "Fortuna Düsseldorf"):
        clubName = "Fortuna Dusseldorf"          
#%%
    elif(clubName == "SL Benfica"):
        clubName = "Benfica" 
    elif(clubName == "Sporting CP"):
        clubName = "Sporting"         
    elif(clubName == "FC Porto"):
        clubName = "Porto" 
    elif(clubName == "SC Braga"):
        clubName = "Braga" 
    elif(clubName == "Vitória de Guimarães"):
        clubName = "Vitória Guimarães" 
    elif(clubName == "Boavista FC"):
        clubName = "Boavista"         
    elif(clubName == "Clube Sport Marítimo"):
        clubName = "Marítimo"         
    elif(clubName == "Portimonense SC"):
        clubName = "Portimonense" 

    elif(clubName == "SC Heerenveen"):
        clubName = "Heerenveen" 
    elif(clubName == "FC Utrecht"):
        clubName = "Utrecht"         
    elif(clubName == "FC Twente"):
        clubName = "Twente"
#%%   
    elif(clubName == "Rangers FC"):
        clubName = "Glasgow Rangers"
    elif(clubName == "Rosenborg BK"):
        clubName = "Rosenborg" 
    elif(clubName == "Malmö FF"):
        clubName = "Malmo" 
    elif(clubName == "HJK Helsinki"):
        clubName = "Helsinki"           
    elif(clubName == "F.C. København"):
        clubName = "Copenhague"      
    elif(clubName == "FC Midtjylland"):
        clubName = "Midtjylland"  
    elif(clubName == "FC Red Bull Salzburg"):
        clubName = "RB Salzburg"
    elif(clubName == "SK Rapid Wien"):
        clubName = "Rapid Viena"
    elif(clubName == "BSC Young Boys"):
        clubName = "Young Boys"       
    elif(clubName == "FC Basel 1893"):
        clubName = "Basel"      
    elif(clubName == "FC Zürich"):
        clubName = "Zurich"
    elif(clubName == "Club Brugge KV"):
        clubName = "Brugge"
    elif(clubName == "Standard de Liège"):
        clubName = "Standard Liege"
    elif(clubName == "RSC Anderlecht"):
        clubName = "Anderlecht"     
    elif(clubName == "KRC Genk"):
        clubName = "Genk"
        
#%%
    elif(clubName == "Zenit Saint Petersburg"):
        clubName = "Zenit" 
    elif(clubName == "Spartak Moskva"):
        clubName = "Spartak Moscou"
    elif(clubName == "CSKA Moskva"):
        clubName = "CSKA"
    elif(clubName == "FC Krasnodar"):
        clubName = "Krasnodar"
    elif(clubName == "FC Lokomotiv Moscow"):
        clubName = "Locomotiv Moscou"   
    elif(clubName == "Dynamo Moskva"):
        clubName = "Dinamo Moscou"              
    elif(clubName == "FC Sochi"):
        clubName = "Sochi"     

    elif(clubName == "FK Partizan"):
        clubName = "Partizan"
    elif(clubName == "Crvena Zvezda"):
        clubName = "Estrela Vermelha"
    elif(clubName == "Ludogorets Razgrad"):
        clubName = "Ludogorets"
    elif(clubName == "Shakhtar Donetsk"):
        clubName = "Shaktar Donetsk"
    elif(clubName == "Dynamo Kyiv"):
        clubName = "Dinamo Kiev"     
#%%      

    elif(clubName == "Galatasaray SK"):
        clubName = "Galatasaray"
    elif(clubName == "Beşiktaş JK"):
        clubName = "Besiktas"
    elif(clubName == "Fenerbahçe SK"):
        clubName = "Fenerbahce"
    elif(clubName == "İstanbul Başakşehir FK"):
        clubName = "Instanbul Basaksehir"
    elif(clubName == "Olympiacos"):
        clubName = "Olympiacos"
    elif(clubName == "AEK Athens"):
        clubName = "AEK"
    elif(clubName == "Panathinaikos FC"):
        clubName = "Panathinaikos"
    elif(clubName == "FC Viktoria Plzeň"):
        clubName = "Viktoria Plzen"          
    elif(clubName == "FK Vardar"):
        clubName = "FK Vardar"       
    elif(clubName == "NK Maribor"):
        clubName = "Maribor" 
    elif(clubName == "FCSB (Steaua)"):
        clubName = "Steaua Bucareste"    
    elif(clubName == "FK Qarabag"):
        clubName = "Qarabag"         
    elif(clubName == "FC Astana"):
        clubName = "Astana"      
    elif(clubName == "Sparta Praha"):
        clubName = "Sparta Praga"
    elif(clubName == "SK Slavia Praha"):
        clubName = "Slavia Praha"   
#%%
    elif(clubName == "KAA Gent"):
        clubName = "Gent"          
    elif(clubName == "Royal Antwerp FC"):
        clubName = "Royal Antwerp"      
    elif(clubName == "Lech Poznań"):
        clubName = "Lech Poznan"          
    elif(clubName == "SK Sturm Graz"):
        clubName = "Sturm Graz"           
    elif(clubName == "FK Bodø/Glimt"):
        clubName = "Bodø/Glimt"           
    elif(clubName == "Molde FK"):
        clubName = "Molde"        
    elif(clubName == "Brøndby IF"):
        clubName = "Brøndby"     
    elif(clubName == "FK Austria Wien"):
        clubName = "Austria Wien"     
###################################################
###################################################
###################################################               
#%%
    elif(clubName == "São Paulo FC"):
        clubName = "São Paulo"
    elif(clubName == "Santos FC"):
        clubName = "Santos"
    elif(clubName == "Atlético Mineiro"):
        clubName = "Atlético-MG"     
    elif(clubName == "SC Internacional"):
        clubName = "Internacional"     
    elif(clubName == "Botafogo FR"):
        clubName = "Botafogo"        
    elif(clubName == "Athletico Paranaense"):
        clubName = "Atlético-PR"        
    elif(clubName == "Fortaleza EC"):
        clubName = "Fortaleza"        
    elif(clubName == "Ceará SC"):
        clubName = "Ceará"    
    elif(clubName == "Ceará SC"):
        clubName = "Ceará" 
    elif(clubName == "Atlético Goianiense"):
        clubName = "Atlético-GO" 
    elif(clubName == "RB Bragantino"):
        clubName = "Bragantino"   
#%%
    elif(clubName == "EC Bahia"):
        clubName = "Bahia" 
    elif(clubName == "América Mineiro"):
        clubName = "América-MG"
    elif(clubName == "EC Bahia"):
        clubName = "Bahia" 
    elif(clubName == "Chapecoense AF"):
        clubName = "Chapecoense"         
    elif(clubName == "Paraná Clube"):
        clubName = "Paraná"
    elif(clubName == "Guarani FC"):
        clubName = "Guarani"       
    elif(clubName == "Criciúma EC"):
        clubName = "Criciúma"        
    elif(clubName == "EC Vitória"):
        clubName = "Vitória"
    elif(clubName == "Paraná Clube"):
        clubName = "Paraná"
    elif(clubName == "Cuiabá EC"):
        clubName = "Cuiabá"
    elif(clubName == "Sport Recife"):
        clubName = "Sport"
    elif(clubName == "Vasco da Gama"):
        clubName = "Vasco"
    elif(clubName == "Náutico"):
        clubName = "Naútico"
#%%
    elif(clubName == "Ituano FC"):
        clubName = "Ituano"   
    elif(clubName == "CS Alagoano"):
        clubName = "CSA"        
    elif(clubName == "Clube de Regatas Brasil"):
        clubName = "CRB"           
    elif(clubName == "Londrina EC"):
        clubName = "Londrina"  
    elif(clubName == "Operário Ferroviário EC"):
        clubName = "Operário-PR"  
    elif(clubName == "Clube do Remo"):
        clubName = "Remo"  
    elif(clubName == "Paysandu SC"):
        clubName = "Paysandu"  
    elif(clubName == "Manaus FC"):
        clubName = "Manaus"  
    elif(clubName == "Mirassol FC"):
        clubName = "Mirassol"  
        
    elif(clubName == "Avaí FC"):
        clubName = "Avaí" 
    elif(clubName == "Tombense FC"):
        clubName = "Tombense" 
    elif(clubName == "Botafogo PB"):
        clubName = "Botafogo-PB" 
    elif(clubName == "Botafogo SP"):
        clubName = "Botafogo-SP" 
    elif(clubName == "Campinense Clube"):
        clubName = "Campinense" 
    elif(clubName == "AD Confiança"):
        clubName = "Confiança" 
    elif(clubName == "EC Santo André"):
        clubName = "Santo André" 
    elif(clubName == "SER Caxias do Sul"):
        clubName = "Caxias do Sul" 
#%% 
    elif(clubName == "Club Atlético Colón"):
        clubName = "Colón"  
    elif(clubName == "Racing Club"):
        clubName = "Racing"
    elif(clubName == "Club Atlético Independiente"):
        clubName = "Independiente"
    elif(clubName == "Club Atlético Lanús"):
        clubName = "Lanús"
    elif(clubName == "Estudiantes de La Plata"):
        clubName = "Estudiantes"
    elif(clubName == "San Lorenzo de Almagro"):
        clubName = "San Lorenzo"
    elif(clubName == "Club Atlético Talleres"):
        clubName = "Talleres"
    elif(clubName == "Club Atlético Banfield"):
        clubName = "Banfield"
    elif(clubName == "Arsenal de Sarandí"):
        clubName = "Arsenal Sarandí"      
        
    elif(clubName == "Club Atlético Huracán"):
        clubName = "Huracán"           
    elif(clubName == "Gimnasia y Esgrima La Plata"):
        clubName = "Gimnasia y Esgrima"    
    elif(clubName == "Unión de Santa Fe"):
        clubName = "Unión de Santa Fe"    
#%%         
    elif(clubName == "Club Olimpia"):
        clubName = "Olimpia"
    elif(clubName == "Club Libertad"):
        clubName = "Libertad"
    elif(clubName == "Colo Colo"):
        clubName = "Colo-Colo"
    elif(clubName == "Universidad de Chile"):
        clubName = "LaU"
    elif(clubName == "Universidad Católica"):
        clubName = "Univ. Católica"
    elif(clubName == "Independiente del Valle"):
        clubName = "I. Del Valle"
    elif(clubName == "Liga de Quito"):
        clubName = "LDU"
    elif(clubName == "CS Emelec"):
        clubName = "Emelec"
    elif(clubName == "Barcelona SC"):
        clubName = "Barcelona-EQU"
    elif(clubName == "Caracas FC"):
        clubName = "Caracas"
    elif(clubName == "Club Universitario de Deportes"):
        clubName = "Universitario"
    elif(clubName == "Club The Strongest"):
        clubName = "The Strongest"
        
    elif(clubName == "Club Cienciano"):
        clubName = "Cienciano"        
    elif(clubName == "Club Deportivo Palestino"):
        clubName = "Palestino"            
    elif(clubName == "Deportivo Táchira FC"):
        clubName = "Deportivo Táchira"     
    elif(clubName == "Club Deportivo Jorge Wilstermann"):
        clubName = "Jorge Wilstermann"                 
    elif(clubName == "Club Always Ready"):
        clubName = "Always Ready"        
    elif(clubName == "Club Nacional"):
        clubName = "Club Nacional"      
    elif(clubName == "FBC Melgar"):
        clubName = "Melgar"            
    elif(clubName == "Club Deportivo Palestino"):
        clubName = "Palestino"        
        
#%%         
    elif(clubName == "Junior FC"):
        clubName = "Junior"
    elif(clubName == "Independiente Medellín"):
        clubName = "I. Medellín"
    elif(clubName == "Independiente Santa Fé"):
        clubName = "Santa Fé" 
    elif(clubName == "Deportes Tolima"):
        clubName = "Tolima"        

###################################################
###################################################
###################################################
#%%
    elif(clubName == "Club América"):
        clubName = "América-MEX"
    elif(clubName == "Guadalajara"):
        clubName = "Chivas Guadalajara"
    elif(clubName == "UNAM Pumas"):
        clubName = "Pumas"
    elif(clubName == "Tigres UANL"):
        clubName = "Tigres"
    elif(clubName == "Deportivo Toluca"):
        clubName = "Toluca"     
    elif(clubName == "Club Atlas"):
        clubName = "Atlas"    
    elif(clubName == "Club Tijuana"):
        clubName = "Tijuana"            
    elif(clubName == "Puebla FC"):
        clubName = "Puebla"               
    elif(clubName == "Gallos Blancos de Querétaro"):
        clubName = "Querétaro"            
    elif(clubName == "Club Necaxa"):
        clubName = "Necaxa"         
    elif(clubName == "Fútbol Club Juárez"):
        clubName = "Juárez"     
#%%         
    elif(clubName == "Seattle Sounders FC"):
        clubName = "Seattle Sounders"
    elif(clubName == "Los Angeles FC"):
        clubName = "Los Angeles FC" 
    elif(clubName == "New York City FC"):
        clubName = "NY City" 
    elif(clubName == "New England Revolution"):
        clubName = "NE Revolution" 
    elif(clubName == "Orlando City Soccer Club"):
        clubName = "Orlando City" 
    elif(clubName == "Inter Miami CF"):
        clubName = "Inter Miami" 
    elif(clubName == "D.C. United"):
        clubName = "DC United" 
    elif(clubName == "Vancouver Whitecaps FC"):
        clubName = "Vancouver Whitecaps" 
    elif(clubName == "New York Red Bulls"):
        clubName = "NY Red Bulls" 
    elif(clubName == "Minnesota United FC"):
        clubName = "Minnesota United"   
    elif(clubName == "Club de Foot Montréal"):
        clubName = "Club Montréal"      
    elif(clubName == "Nashville SC"):
        clubName = "Nashville"        
    elif(clubName == "Chicago Fire Football Club"):
        clubName = "Chicago Fire"     
###################################################
###################################################
###################################################        
#%%  
    elif(clubName == "Shanghai Port"):
        clubName = "Shanghai SIPG"
    elif(clubName == "Guangzhou"):
        clubName = "Ghuangzhou Evergrande"
    elif(clubName == "Shandong Taishan"):
        clubName = "Shandong Luneng"
    elif(clubName == "Jeonbuk Motors"):
        clubName = "Jeonbuk Hyundai"
    elif(clubName == "Al Ain"):
        clubName = "Al Ain-EAU"
    elif(clubName == "Al Sadd SC"):
        clubName = "Al Sadd"
    elif(clubName == "Al Hilal SC"):
        clubName = "Al Hilal"
    elif(clubName == "Al Ahli Jeddah"):
        clubName = "Al Ahli"        
    elif(clubName == "Al Duhail SC"):
        clubName = "Al Duhail" 
#%%        
    elif(clubName == "Suwon Samsung Bluewings"):
        clubName = "Suwon Samsung" 
    elif(clubName == "Melbourne City FC"):
        clubName = "Melbourne City" 
#%%        
    elif(clubName == "Zamalek SC"):
        clubName = "Zamalek"
    elif(clubName == "TP Mazembe"):
        clubName = "Mazembe" 
    elif(clubName == "Wydad AC"):
        clubName = "Wydad Casablanca"            

         
     
        
    return clubName