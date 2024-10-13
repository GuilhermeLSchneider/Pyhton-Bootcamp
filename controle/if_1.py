#O Python é dependente da indentação para definir blocos de código.

nota = float(input('Digite a nota do aluno: '))
comportado = True if input('O aluno é comportado? (s/n) ') == 's' else False

if nota >= 9.5 and comportado:
    print('Aprovado! Parabéns')
    print('Quadro de Honra')
elif nota >= 6 and comportado:
    print('Aprovado! Parabéns')
elif nota >= 4 and comportado:
    print('Recuperação')
else:
    print('Reprovado!')
