# Estrutura de controle do while

notaF = 0
qtde = 0
nota = 0

while notaF != -1:
    notaF = float(input("Digite a nota do aluno, e -1 para finalizar: "))
    if notaF != -1:
        qtde+=1
        nota += notaF

print(f'A média das notas da turma é: {nota/qtde}')