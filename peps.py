
### DELETANDO ARQUIVO ZIP ANTIGO
import os
def etc():
    path = "C:\\Users\\Bruno\\Downloads\\"
    dir = os.listdir(path)
    for file in dir:
        if file == '202001_PEP.zip':
            os.remove(file)
etc()


###BUSCANDO O ARQUIVO NA BASE DE DADOS DA RECEITA

# Python versão 3.4.0

### PARA O SELENIUM

# Para o Chrome:
# - Importar módulo chromedriver em https://chromedriver.storage.googleapis.com/index.html?path=72.0.3626.69/
# - Extrair e colocar o arquivo dentro da pasta do Python 3.4

# Instalar o pip e importar o módulo Selenium:
# (no local do arquivo, instalar o get-pip.py)

# Página do selenium:
# https://translate.google.com.br/translate?hl=pt-BR&sl=en&u=https://stackoverflow.com/questions/22529433/ie-driver-download-location-link-for-selenium&prev=search

# Para o Internet Explorer:
# - Baixar o módulo em https://translate.google.com.br/translate?hl=pt-BR&sl=en&u=https://stackoverflow.com/questions/22529433/ie-driver-download-location-link-for-selenium&prev=search
# - Extrair e colocar o arquivo dentro da pasta Scripts da pasta do Python 3.4


### PARA O CAPTCHA

# Instalar módulo Pillow no pip dentro da pasta Scripts
# Instalar módulo lxml no pip dentro da pasta Scripts
# Instalar módulo cssselect no pip dentro da pasta Scripts


import selenium
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Login/senha
ano = "2020"
meses = "JANEIRO"

# Inicializacao do driver Firefox, Chrome ou Ie
driver = webdriver.Chrome()

# Abrindo a pagina do facebook
driver.get("http://www.portaldatransparencia.gov.br/download-de-dados/pep")

# Entrada do codigo
elmnt = driver.find_element_by_id("links-anos")
elmnt.send_keys(ano)

# Entrada do digito
elmnt = driver.find_element_by_id("links-meses")
elmnt.send_keys(meses)

# Pressionando o botão de login
elmnt = driver.find_element_by_id("btn")
elmnt.send_keys(Keys.ENTER)

time.sleep(15)

# Fechando o browser
driver.close()

# Fechando o driver
driver.quit()



###DESCOMPACTANDO
import zipfile, os
os.chdir ('C:\\Users\\Bruno\\Downloads')  #vai para a pasta que contém o exemplo.zip
pep = zipfile.ZipFile ('C:\\Users\\Bruno\\Downloads\\202001_PEP.zip')
pep.extractall('C:\\Users\\Bruno\\Downloads\\PEP') #extrai todos os arquivos para a pasta atual
pep.close()


###LENDO CSV
import csv
arquivo = open('C:\\Users\\Bruno\\Downloads\\PEP\\202001_PEP.csv')
peps = csv.DictReader(arquivo)
for pep in peps:
    print(pep)


import csv
with open('C:\\Users\\Bruno\\Downloads\\PEP\\202001_PEP.csv') as csv_file:
    csv_reader = csv.reader(csv_file)
    cabecalho = True
    for row in csv_reader:
        if cabecalho:
            print("Nomes das colunas: ".format(", ".join(row)))
            cabecalho = False
        else:
            print(format(", ".join(row)))


#Jogar o texto dentro de uma lista
import csv
with open('C:\\Users\\Bruno\\Downloads\\PEP\\202001_PEP.csv', newline='') as f:
    reader = csv.reader(f, skipinitialspace=True)
    rows = list(reader)

pesquisa = str(input("Digite a palavra para pesquisa: ")).upper()

cont = 0
lista = []
for g in range(len(rows)):
    for i in rows[g]:
        if pesquisa in i:
            print(i)




### BANCO DE DADOS
import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="recadastro")
cursor = mydb.cursor()
query = ("SELECT * FROM SEQUENCIAS")
cursor.execute(query)
for PONTO in cursor:
    print(PONTO)
cursor.close()
mydb.close()

