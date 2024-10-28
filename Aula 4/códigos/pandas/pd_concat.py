import numpy as np
import pandas as pd

# Definição dos dataframes
df1 = pd.DataFrame({"A": ['A0', 'A1', 'A2', 'A3'],
                    "B": ['B0', 'B1', 'B2', 'B3'],
                    "C": ['C0', 'C1', 'C2', 'C3'],
                    "D": ['D0', 'D1', 'D2', 'D3']},
                    index=[0, 1, 2, 3])

df2 = pd.DataFrame({"A": ['A4', 'A5', 'A6', 'A7'],
                    "B": ['B4', 'B5', 'B6', 'B7'],
                    "C": ['C4', 'C5', 'C6', 'C7'],
                    "D": ['D4', 'D5', 'D6', 'D7']},
                    index=[4, 5, 6, 7])

df3 = pd.DataFrame({"A": ['A8', 'A9', 'A10', 'A11'],
                    "B": ['B8', 'B9', 'B10', 'B11'],
                    "C": ['C8', 'C9', 'C10', 'C11'],
                    "D": ['D8', 'D9', 'D10', 'D11']},
                    index=[8, 9, 10, 11])

# Importante notar que os dataframes possuem tamanho e colunas iguais,
# isso evita problemas de concatenação ou falta de dados
print(pd.concat([df1, df2, df3]))

# No caso abaixo, a concatenação é feita por coluna
# Ele produz um resultado utilizando os índices de linha dos dataframes
print(pd.concat([df1, df2, df3], axis=1))

# Mesclar
# Permite juntar tabelas de acordo com uma coluna em comum
esquerda = pd.DataFrame({"key": ['K0', 'K1', 'K2', 'K3'],
                         'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']})

direita = pd.DataFrame({"key": ['K0', 'K1', 'K2', 'K3'],
                        'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']})

# O parametro how é similar ao SQL (inner join), onde inner é a interseção
# O parametro on é a chave de junção da nossa tabela (key)
print(pd.merge(esquerda, direita, how='inner', on='key'))

# Caso existisse duas ou mais chaves de junção, poderiamos passar uma tupla no parametro on
# Exemplo: print(pd.merge(esquerda, direita, how='inner', on=['key1', 'key2']))

# Join
# Permite juntar tabelas de acordo com os índices
esquerda = pd.DataFrame({'A': ['A0', 'A1', 'A2', 'A3'],
                         'B': ['B0', 'B1', 'B2', 'B3']},
                        index=['K0', 'K1', 'K2', 'K3'])

direita = pd.DataFrame({'C': ['C0', 'C1', 'C2', 'C3'],
                        'D': ['D0', 'D1', 'D2', 'D3']},
                        index=['K0', 'K1', 'K4', 'K5'])

# O join pegou os índices em comum entre as tabelas e juntou as colunas,
# caso não exista um índice em comum, ele preenche com NaN
print(esquerda.join(direita))
# O parametro how='outer' faz com que ele pegue todos os índices, mesmo que não existam em comum
print(esquerda.join(direita, how='outer'))