import numpy as np;

# Vídeo começa com uma introdução sobre acesso a elementos de arrays

vetor1 = np.arange(50).reshape(5, 10)

# print(vetor1)

# Acesso a elementos de uma matriz
# Onde o primeiro colchete indica a linha e o segundo colchete indica a coluna
# print(vetor1[:3][:])
# # Pode ser acessado de outra forma
# print(vetor1[:, :])

# Importante notar que essa atribuição de valores é por REFERÊNCIA
# vetor2 = vetor1[:][:]
# Para fazer uma cópia do array, é necessário utilizar o método copy()
# vetor2 = vetor1.copy()

# vetor1[:1] = 100
# print(vetor1)

# Fatiamento de arrays -> Acessando um subconjunto de elementos de um array
# Acessa a linha 1 até a 3, e a coluna 0 até a 4
# print(vetor1[1:4, :5])

# vetor_boolean = vetor1 >= 20
# print(vetor_boolean)
# Retorna um vetor com os valores que são True
# print(vetor1[vetor_boolean])

# Acessando os valores na diagonal da matriz vetor1
# print(np.diag(vetor1))

# Acessando os valores na diagonal inversa da matriz vetor1
# print(np.diag(vetor1[::-1]))
