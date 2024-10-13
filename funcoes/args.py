def soma(*args):
    total = 0
    for i in args:
        total += i
    return total

def resultado_final(**kwargs):
    status = 'aprovado' if kwargs['nota'] >= 6 else 'reprovado'
    return f'{kwargs["nome"]} está {status}'