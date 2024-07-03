# Desafio 

nome = input('Digite seu nome: ')
idade = int(input('Digite sua idade: '))

quantidade_de_letras = str(len(nome))

idade_futuro = str(idade + 5)

print('Olá ' + nome + ', como vai?')
print('Seu nome é composto por ' + quantidade_de_letras + ' letras.')
print('Em 5 anos, você terá ' + idade_futuro + ' anos.')