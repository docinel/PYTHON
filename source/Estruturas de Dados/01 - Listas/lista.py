frutas = ["banana", "maca", "laranja"]
print(frutas)
print(frutas[0])
print('---' * 10)

letras = list("abacaxi")
print(letras)
print(letras[6])
print(len(letras))
print('---' * 10)
print(letras[2:])
print(letras[:3])
print(letras[2:4])
print(letras[::-1])
print('---' * 10)

numeros = list(range(10))
print(numeros)
print('---' * 10)

for frutas in frutas:
    print(frutas)
print('---' * 10)

for indice, fruta in enumerate(frutas):
    print(f"{indice}: {fruta}")  # print(indice, fruta)
print('---' * 10)

# Lista de Compreesão
numeros = [1, 4, 9, 16, 25, 35, 78, 100, 27, 36, 45, 54, 63, 72, 81, 90, 99]
pares = [x for x in numeros if x % 2 == 0]
print(pares)
print('---' * 10)