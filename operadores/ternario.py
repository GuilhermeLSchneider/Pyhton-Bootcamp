b1 = True
# b1 = False
# combustivel = 0
combustivel = 50

status = 'Dirigindo' if b1 and combustivel >= 10 else 'A pé'

# print(status)
print(f'{status}')