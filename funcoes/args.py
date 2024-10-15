#Os args são argumentos que podem ser passados para uma função sem a necessidade de definir quantos são.
#O * é um operador de desempacotamento, que permite que uma função receba um número variável de argumentos.
def soma(*args):
    total = 0
    for i in args:
        total += i
    return total

# Os kwargs são argumentos que podem ser passados para uma função sem a necessidade de definir quantos são.
# O ** é um operador de desempacotamento, que permite que uma função receba um número variável de argumentos nomeados.
def resultado_final(**kwargs):
    status = 'aprovado' if kwargs['nota'] >= 6 else 'reprovado'
    return f'{kwargs["nome"]} está {status}'