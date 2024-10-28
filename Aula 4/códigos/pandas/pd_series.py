import numpy as np
import pandas as pd

labels = ['a', 'b', 'c']
my_data = [10, 20, 30]
arr = np.array(my_data)
d = {'a': 10, 'b': 20, 'c': 30}

# Importante notar que o Series se assemelha a um dicionário
print(pd.Series(data=my_data, index=labels))

serie = pd.Series(data=my_data, index=labels)
print(serie['b'])

# Alterar a ordem dos parâmetros faz com que os dados sejam mostrados de forma diferente
# Em questão de visualização, pd.Series(data=labels, index=my_data) != pd.Series(data=my_data, index=labels)

print(pd.Series(data=labels, index=arr))

carros1 = pd.Series(data=[1, 2, 3, 4], index=['EcoSport', 'Fiesta', 'Focus', 'Fusion'])
carros2 = pd.Series(data=[1, 2, 3, 4, 5], index=['Fiesta', 'EcoSport', 'Fusion', 'Focus', "Civic"])
# Ao somar duas Series, o Pandas irá somar os valores que possuem o mesmo índice
# Caso um dos índices não exista em uma das Series, o valor será considerado NaN

print(carros1 + carros2)