# Data Scrapper

## Descrição do Projeto 

 Arquivos em Python para extrair dados online de jogadores do banco de dados dos sites "SoFifa" e "SoccerWiki" em arquivos .csv, para ser usado no meu jogo de Football Manager.

## Como usar o Projeto

 O arquivo pega dados dos sites "SoFifa" e "SoccerWiki" e usando o BeautifulSoup do Python procura pelas tags Html com as informações necessárias de cada jogador como nome, idade, posição e potencial para salvar em um arquivo ".csv". Finalizado, seu processo os arquivos gerados poderm ser importados e usados no aplicativo de football manager que estou desenvolvendo com mais de 400 times sempre atualizados.

## Como Executar o projeto

Pré requisito ter o Python instalado com as bibliotecas de pandas e BeautifulSoup.

 1º Baixe todos os arquivos
 2º Com um compilador python execute o arquivo "fifa_scrapper.py" e então serão gerados os arquivos ".csv" com os jogadores dos clubes na pasta "data".
