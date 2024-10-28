#Atribuição de funções a variáveis

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

# somar = soma
# print(somar(2, 3))

#Passagem de funções como argumentos
def operacao_aritmetica(fn, op1, op2):
    return fn(op1, op2)

# result = operacao_aritmetica(soma, 9, 19)
# print(result)

# result = operacao_aritmetica(subtracao, 19, 9)
# print(result)

#A ideia de funções identadas serve para reduzir tempo de processamento
#fazendo com que não seja necessario executar a função inteira do 0, toda vez que for chamada
def soma_parcial(a):
    def concluir_soma(b):
        return a + b
    return concluir_soma