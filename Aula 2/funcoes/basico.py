
#Pyhton não faz sobrecarga de métodos, ou seja, não podemos ter dois métodos com o mesmo nome
# def saudacao():
#     print('Olá mundo!')

def saudacao(nome):
    print(f'Olá {nome}!')

#Preferencia por retornar valores e não printar diretamente na tela
def soma_e_multi(a, b, x):
    return a + b * x