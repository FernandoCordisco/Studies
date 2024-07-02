#Soma:

numeros = [1, 2, 4, 6, 7]
soma = 0
tam_list_numeros = len(numeros)

for numero in numeros:
    soma += numero

media = soma / tam_list_numeros

print(f'A soma dos valores foi de {soma}, com a media de {media}')

    
#Função de soma:
print(sum(numeros))