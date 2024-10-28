#Em Python é necessário escrever as operações lógicas and, or e not.
#Ao utilizar '|' ou '&', o Python não irá reconhecer a operação lógica.

b1 = True
b2 = False
b3 = True

print(b1 and b2)
print(b1 and b2 and b3)
print(b1 and b3)

print(b1 or b2)
print(b1 or b2 or b3)
print(b1 or b3)

print(not b1)
print(not b2)
print(b1 and not b2)