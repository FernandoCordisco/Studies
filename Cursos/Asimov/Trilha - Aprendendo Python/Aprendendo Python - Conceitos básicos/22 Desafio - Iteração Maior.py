numeros = [1, 2, 4, 6, 7]
maximo = numeros[0]

for numero in numeros:
    if maximo < numero:
        maximo = numero

print(f'O valor máximo é {maximo}')