# Funções map e reduce
from functools import reduce

# def somar_bonus(nota):
#     return nota + 1.5

def somar_nota(bonus):
    def somar(nota):
        return nota + bonus
    return somar

notas = [6.4, 7.2, 5.8, 8.4, 6.5, 7.0, 5.5]
notas_finais = map(somar_nota(1.5), notas)
notas_finais2 = map(somar_nota(1.6), notas)

print(list(notas_finais))
print(list(notas_finais2))

def total_nota(nota, acumulador):
    return nota + acumulador

# A função reduce recebe dois argumentos, o primeiro é a função que será aplicada 
# (normalmente consiste em uma variavel que acumula o valor e outra que acessa os valores na lista) 
# e o segundo é a lista que será percorrida
print(reduce(total_nota, notas, 0)) # 0 é o valor inicial do acumulador
