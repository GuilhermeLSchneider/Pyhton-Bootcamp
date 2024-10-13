# for i in range(10):
#     print(i + 1)

# for i in range(1, 11): # Aqui, o range começa em 1 e vai até 10, não contando o 11
#     print(i)

# for i in range(1, 11, 2): # Aqui, o range começa em 1 e vai até 10, não contando o 11, pulando de 2 em 2
#     print(i)

for i in range(10, 0, -1): # Aqui, o range começa em 10 e vai até 1, não contando o 0, pulando de -1 em -1
    print(i)

num = [1, 2, 3, 4, 5]

# num = ("Aula 1 Curso Python")
# No exemplo acima, ao utilizar ela no for, 
# ele irá percorrer cada letra da string, separando-as por espaço'

#Note que aqui não é necessário o uso de range, pois o for já percorre a lista, similar ao foreach de outras linguagens
for n in num:
    print(n, end=' ') 
    # Caso queira, o end=' ' faz com que o print não pule linha, mas sim coloque um espaço entre os elementos

carro = {
    "marca": "Ford",
    "modelo": "Fusion",
    "ano": 2023
}

for info, carac in carro.items():
    print(info, '=>', carac) #Pode ser acessado diretamente com o carro[info]
    # Aqui, o for percorre as chaves do dicionário, e o carro[info] retorna o valor da chave atual

#Há também a possibilidade de utilizar dois fors aninhados
pessoas = ["Guilherme", "João", "Maria", "José"]
caracteristicas = ["Legal", "Chato", "Engraçado", "Sério"]

for p in pessoas:
    for c in caracteristicas:
        print(p, 'é', c)
        # Aqui, o for percorre a lista de pessoas, e para cada pessoa, percorre a lista