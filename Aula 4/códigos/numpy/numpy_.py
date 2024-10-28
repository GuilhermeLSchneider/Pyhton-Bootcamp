import numpy as np;

# Criando um array

# vetor1 = ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# np.array(vetor1)

# matriz1 = ([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# print(np.array(matriz1))

# np.arange(0, 15)
# np.arange(0, 10, 2)

# # Criando uma matriz de 0's
# print(np.zeros((5,5)))

# # Criando uma matriz de 1's
# print(np.ones((5,5)))

# # Criando uma matriz identidade
# print(np.eye(5))

# # Linspace - Retorna um número de valores igualmente distribuídos no intervalo especificado
# print(np.linspace(0, 10, 5))

# # Rand - Retorna um número de valores de uma distribuição uniforme
# print(np.random.rand(5))
# print(np.random.rand(5) * 100)
# print(np.random.rand(5) / 2)
# print(np.random.rand(5, 4))
# print(np.random.rand(5, 4, 3))

# Randn - Retorna um número de valores de uma distribuição normal
# print(np.random.randn(4))

# Transformações
# print(np.random.rand(5) * 100)
# print(np.round(np.random.rand(5) * 100, 2))
# print(np.power(np.random.rand(5), 2))

# print(np.random.randint(0, 100, 20))

# randarray = np.random.rand(25)
# print(randarray)
# print(np.reshape(randarray, (5, 5))) # Transforma o array em uma matriz 5x5, no entanto, o array original não é alterado
# print(randarray = randarray.reshape(5, 5)) # Transforma o array em uma matriz 5x5, e o array original é alterado

# print(randarray.shape) # Retorna o formato do array
# print(randarray.max()) # Retorna o maior valor do array
# print(randarray.min()) # Retorna o menor valor do array
# print(randarray.argmax()) # Retorna o índice do maior valor do array
# print(randarray.argmin()) # Retorna o índice do menor valor do array