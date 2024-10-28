import numpy as np 
import pandas as pd

data = np.random.seed(101)
dataframe = pd.DataFrame(np.random.randn(5,4), index= 'A B C D E'.split(), columns= 'W X Y Z'.split())
print(dataframe)

# Os tipos de dados de um dataframe são conjuntos de series
print(dataframe['W'])
print(dataframe[['W', 'X']])

# Adicionando colunas ao dataframe
dataframe['Soma Col W&X'] = dataframe['W'] + dataframe['X']
print(dataframe)

# Removendo colunas
dataframe.drop("Soma Col W&X", axis=1, inplace=True) 
# Importante notar a utilização do inplace para que a alteração seja feita no dataframe
print(dataframe)

print(dataframe.loc['A']) # Acessa a linha A
print(dataframe.loc['A', 'W']) # Acessa o valor da linha A e coluna W
# Para que essa função funcione, é necessário utilizar index de linhas ou linha e coluna,
# não é possível passar apenas colunas
print(dataframe.loc[['A', 'B'], ['W', 'X']]) # Acessa as linhas A e B e as colunas W e X

print(dataframe.iloc[2:4, 0:5]) # Acessa a linha 0, a partir do índice de numero, similar ao numpy
