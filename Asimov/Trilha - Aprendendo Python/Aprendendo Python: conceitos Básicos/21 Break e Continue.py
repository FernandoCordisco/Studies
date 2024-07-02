n = 0

while n < 10:
    print(f'O valor de n é: {n}')

    n += 1

    if n == 5:
        break

print('\n\n')

for i in range(-6, 5):
    if i == 0:
        continue
    resultado = 1 / i
    print(f'O resultado de 1 dividido por {i} é: {resultado}')