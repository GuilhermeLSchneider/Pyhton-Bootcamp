import numpy as np
import pandas as pd

# Utilização de métodos de leitura de tipos de dados
# O sep=',' é utilizado para indicar que o arquivo é separado por vírgula
df = pd.read_csv('https://people.sc.fsu.edu/~jburkardt/data/csv/airtravel.csv', sep=',')
# print(df)

# df.to_csv('airtravel.csv', sep=';', decimal=',') # Salva o dataframe em um arquivo csv

# Caso o arquivo possua mais de uma aba, é possível utilizar o parâmetro sheet_name para indicar qual aba será lida
#df = pd.read_excel('https://people.sc.fsu.edu/~jburkardt/data/xlsx/airtravel.xlsx', sheet_name='Sheet1')
#Importante notar que na leitura de arquivos excel, caso exista formatação, ela será perdida

# df.to_excel('airtravel.xlsx', sheet_name='Sheet1') # Salva o dataframe em um arquivo excel

df2 = pd.read_html('https://www.fdic.gov/bank/individual/failed/banklist.html') # Lê tabelas de um site
print(type(df2))
# print(df2[0])
# print(df2[0]['City'])