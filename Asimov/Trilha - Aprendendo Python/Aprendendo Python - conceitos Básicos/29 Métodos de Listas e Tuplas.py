#Metodos de tuplas

tup = (0, 0, 0, 1, 0, 1, 0)

print(tup.index(1))

print(tup.count(0))

#Metodos de listas

l1 = [0, 0, 0, 1, 0, 1, 0]

l2 = l1.copy()

l1.clear()

print(f'Lista 1 = {l1} / Lista 2 = {l2}')

for n in range(5):
    l1.append(n * 2)

print(l1)

l1.append('Hello')
print(l1)

valores = [10, 20, -50, 0, 1, -80]

valores_positivos = list()

for valor in valores:
    if valor > 0:
        valores_positivos.append(valor)

print(valores_positivos)

numeros = [1, 2, 3]

numeros.extend([4, 5, 6])

print(numeros)

numeros_novos = numeros + [7, 8, 9]

print(numeros_novos)

vogais = ['a', 'i', 'o', 'u']
vogais.insert(1, 'e')

print(vogais)

numeros.pop()
print(numeros)

numeros.pop(0)
print(numeros)

numeros.reverse()
print(numeros)

valores.sort()
print(valores)

valores.reverse()
print(valores)