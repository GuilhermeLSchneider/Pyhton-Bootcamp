import numpy as np 
import pandas as pd

data = np.random.seed(101)
dataframe = pd.DataFrame(np.random.randn(5,4), index= 'A B C D E'.split(), columns= 'W X Y Z'.split())
print(dataframe)

# print(dataframe > 0)
# # ou também
# print(dataframe[dataframe > 0])
# # No entanto, um o primeiro comando retorna um DataFrame com valores true or false, 
# # enquanto o segundo retorna um DataFrame com valores numéricos, alterando onde o valor não satisfaz a condição.

# print(dataframe[dataframe["W"] > 0]["Y"]) # Retorna a coluna Y onde o valor da coluna W é maior que 0
# # ou também, para simplificar um pouco
# bool_w = dataframe['W'] > 0
# print(dataframe[bool_w]['Y'])

print(dataframe[(dataframe['W'] > 0) & (dataframe['Y'] > 1)]) # Retorna os valores que satisfazem as duas condições
# Além disso, é importante notar o uso do operador & para comparação de DataFrames,
# pois o operador and não é capaz de comparar DataFrames que não sejam booleanos.
# Pode-se usar o operador | para comparação de DataFrames, que é o operador or.

# Adicionando uma nova coluna
col = ['Brasil', 'Argentina', 'Chile', 'Peru', 'Uruguai']
dataframe['Países'] = col
print(dataframe)

print(dataframe.set_index('Países')) # inplace=True para alterar o DataFrame original