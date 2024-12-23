from functools import reduce

alunos = [
    {'nome': 'Benio', 'nota': 8.5},
    {'nome': 'João', 'nota': 7.2},
    {'nome': 'Maria', 'nota': 6.5},
    {'nome': 'José', 'nota': 9.0},
    {'nome': 'Ana', 'nota': 5.5},
    {'nome': 'Paulo', 'nota': 4.7},
    {'nome': 'Pedro', 'nota': 6.3},
    {'nome': 'Carla', 'nota': 8.1},
    {'nome': 'Marta', 'nota': 7.7},
    {'nome': 'Luiz', 'nota': 6.9}
]

verifica_aluno_aprovado = lambda aluno: aluno['nota'] >= 7
# verifica_aluno_honra = lambda aluno: aluno['nota'] >= 9
obter_nota = lambda aluno: aluno['nota']
obter_nomes = lambda aluno: aluno['nome']


# A função filter percorre a lista e aplica a função lambda a cada elemento, 
# retornando apenas os elementos que satisfazem a condição
aprovados = list(filter(verifica_aluno_aprovado, alunos))
# alunos_honra = filter(verifica_aluno_honra, alunos)
nota_alunos_aprovados = map(obter_nota, aprovados)
nome_alunos_aprovados = map(obter_nomes, aprovados)

print(list(aprovados))
print(list(nota_alunos_aprovados))
print(list(nome_alunos_aprovados))
# print(list(alunos_honra))