idade = 20
texto = "Sua idade é: "

# As f-strings permitem incluir expressões dentro de chaves {}
print(f'{texto} {idade}')

# Declaração de variáveis em letra maiúscula (convenção)

PI = 3.141592
RAIO = float(input('Digite o raio de uma circunferência? '))
AREA = PI * pow(RAIO, 2)

print(f'O valor da circunferência é: {AREA} m².')