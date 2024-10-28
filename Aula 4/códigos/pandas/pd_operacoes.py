import numpy as np
import pandas as pd

df1 = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 7, 8], 
                    'col2': [799, 299, 399, 499, 499, 699, 199, 399], 
                    'col3': ['2020-01-01', '2020-01-01', '2020-01-01', '2020-01-03', '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-05']})
# print(df1)
# Verifica os valores únicos da coluna
# print(df1['col2'].unique()) # -> similar ao np.unique(df1['col2']) do numpy
# print(df1['col3'].unique())

# # Verifica a quantidade de valores únicos
# print(df1['col2'].nunique()) # -> similar ao len(np.unique(df1['col2'])) do numpy
# print(df1['col3'].nunique())

# # União dos dois itens acima
# print(df1['col2'].value_counts()) # -> similar ao np.unique(df1['col2'], return_counts=True) do numpy
# print(df1['col3'].value_counts())

# # É importante notar que a consulta é feita a partir do mesmo dataframe,
# # visto que utilizar o df1['col2'] > '300,00' retorna valores booleanos
# print(df1[(df1['col2'] > 300)])
# print(df1[(df1['col2'] > 300) & (df1['col3'] > '2020-01-02')])

def vezes2(x):
    return x * 2

print(df1['col2'].apply(vezes2))
print(df1['col2'].apply(lambda x: x * 2)) # É possível utilizar funções lambda também

# del df1['col1'] # Deleta a coluna
print(df1.columns)
print(df1.index) # Retorna a quantidade de linhas do dataframe

print(df1.sort_values(by='col2')) # -> não altera o dataframe original, utilizando o inplace=True, ele altera

print(df1.isnull()) # Verifica se existem valores nulos
print(df1.dropna()) # Remove valores nulos, eliminando a linha por completo

df2 = pd.DataFrame({'col1': [1, 2, 3, 4, 5, 6, 7, 8], 
                    'col2': [np.nan, 299, 399, 499, np.nan, 699, np.nan, 399], 
                    'col3': ['2020-01-01', '2020-01-01', '2020-01-01', np.nan, '2020-01-02', '2020-01-02', '2020-01-03', '2020-01-05']})

print(df2)

print(df2['col2'].fillna(value=df2['col2'].mean())) # Preenche os valores nulos com a média da coluna
print(df2)

print(df2.pivot_table(values='col2', index='col1', columns='col3')) # Cria uma tabela dinâmica, reordenando os valores