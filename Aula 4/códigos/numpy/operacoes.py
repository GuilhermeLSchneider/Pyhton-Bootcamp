import numpy as np

vetor = np.arange(20)
print(vetor)

print(vetor + vetor)
print(vetor - vetor)
print(vetor * vetor)
# Com o numpy, algumas operações geram warnings ao invés de erros, como a divisão por 0
# Fazendo com que ela não interrompa a execução do código
print(vetor / vetor)
print(vetor ** 2)
print(vetor % 2)

# Funções matemáticas
print(np.sqrt(vetor))
print(np.exp(vetor))

# Média
print(np.mean(vetor))
# Desvio padrão
print(np.std(vetor))

# https://numpy.org/doc/stable/reference/ufuncs.html