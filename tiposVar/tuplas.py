modelo_carros = ("Fusca", "Brasilia", "Opala", "Chevette")

print("Equinox" in modelo_carros)
print("Fusca" in modelo_carros)

print(modelo_carros[1:3])
#Mostra o modelos dos carros de 1 a 3, sem incluir o 3

print(modelo_carros[0:3:2]) 
#Mostra o modelo dos caros de 0 a 3, sem inlcuir o 3 
#(aqui nesse caso o item na terceira posição nem seria exibido) e pulando de 2 em 2

print(modelo_carros[2:]) 
#Mostra o modelo dos carros de 2 até o final

print(modelo_carros[:3])
#Mostra o modelo dos carros do início até o 3, sem incluir o 3

print(modelo_carros)
print(type(modelo_carros))