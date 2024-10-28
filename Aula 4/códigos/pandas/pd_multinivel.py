import numpy as np
import pandas as pd

outside = ['G1', 'G1', 'G1', 'G2', 'G2', 'G2']
inside = [1, 2, 3, 1, 2, 3]

# O método zip cria uma lista de tuplas, onde cada tupla é composta por um elemento de cada lista
hier_index = list(zip(outside, inside))
# O método pd.MultiIndex.from_tuples cria um índice multinível a partir de uma lista de tuplas
hier_index = pd.MultiIndex.from_tuples(hier_index)

# Aqui, os valores G1 e G2 são os valores do primeiro nível do índice, 
# enquanto 1, 2 e 3 são os valores do segundo nível
dataf = pd.DataFrame(np.random.randn(6, 2), index=hier_index, columns=['A', 'B'])
print(dataf)

print(dataf.loc['G1']) # Retorna as linhas contidas no índice G1
print(dataf.loc['G1'].loc[1]) # É possível concatenar os locs para acessar valores mais específicos

print(dataf.index.names) # Nesse caso, os índices não possuem nome
dataf.index.names = ['Grupo', 'Número']

# É mais interessante utilizar o xs por conta de não ser necessário passar todos os níveis do índice
print(dataf.xs('G1'))
print(dataf.xs(1, level='Número'))