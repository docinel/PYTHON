carros = ("gol", "ferrari", "palio", "fiat", "gol", "ferrari")
print(carros)
print(carros[0])
print(len(carros))
print('---' * 10)

for carro in carros:
    print(carro)
print('---' * 10)

lista_unica = set(carros)
print(lista_unica)
print('---' * 10)

lista_unica = list(set(carros))
print(lista_unica)
print('---' * 10)
print(lista_unica[1:3])
