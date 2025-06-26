nome = input('Qual o seu nome? \nDigite seu nome: ')
idade = int(input('Qual a sua idade? \nDigite sua idade: '))

quantidade_de_letras = str(len(nome))

idade_futuro = str(idade + 5)

print('-' * 10)
print(f'Olá, {nome}, como vai?')
print(f'Seu nome é composto por {quantidade_de_letras} letras.')
print(f'Em 5 anos, você terá {idade_futuro} anos.')
print('-' * 10)