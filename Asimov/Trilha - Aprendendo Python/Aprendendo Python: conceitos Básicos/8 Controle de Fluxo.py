idade = int(input('Digite sua idade: '))

if idade < 18:
    print('Você é menor de idade')
    print('Você não pode dirigir e nem beber!')

elif idade == 18:
    print('Você tem exatamente 18 anos')

else:
    print('Você é maior de idade')