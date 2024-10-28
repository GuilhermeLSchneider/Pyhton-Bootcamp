import numpy as np
import pandas as pd

dic = {'A': [1, 2, np.nan], 'B': [5, np.nan, np.nan], 'C': [1, 2, 3]}

df = pd.DataFrame(dic)
print(df)

print(df.dropna()) # Remove todas as linhas que possuem valores NaN
print(df.dropna(thresh=2)) # Remove todas as linhas que possuem 2 ou mais valores NaN
# Importante salientar que a alteração não é feita no dataframe original, a menos que o parâmetro inplace seja True

# print(df.fillna(value='0')) # Preenche todos os valores NaN com o valor passado
print(df['A'].fillna(value=df['A'].mean())) # Preenche os valores NaN da coluna A com a média dos valores da coluna A

# É possível utilizar a função method para preencher os valores NaN com base em valores anteriores ou posteriores
print(df.fillna(method='ffill')) # -> ForwardFill Preenche os valores NaN com o valor da célula anterior
print(df.fillna(method='bfill')) # -> BackwardsFill Preenche os valores NaN com o valor da célula posterior