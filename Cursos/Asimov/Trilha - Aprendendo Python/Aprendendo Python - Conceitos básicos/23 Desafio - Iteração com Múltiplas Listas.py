#Desafio 1

valores1 = [1, 3, 5, 8, 10]
valores2 = [1, 2, 4, 7, 10]

for valor1 in valores1:
    for valor2 in valores2:
        if valor1 == valor2: 
            print(f'O valor {valor1} aparece nas duas listas.')

#desafio 2

lista1 = ['xx', 10, True]
lista2 = ['xx', False, 0]

elemento_em_comum = False

for valor1 in lista1:
    if elemento_em_comum:
        break
    
    for valor2 in lista2:
        if valor1 == valor2: 
            elemento_em_comum = True
            break

if elemento_em_comum:
    print('As listas possuem elemento em comum.')

else:
    print('As listas não possuem elemento em comum.')
