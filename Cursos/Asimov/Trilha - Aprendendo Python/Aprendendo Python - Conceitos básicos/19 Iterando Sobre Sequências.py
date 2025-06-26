valores = [10, 20, 30, 40, 50, 60]

for valor in valores:
    print(f'O valor é: {valor}')


nome = 'Fernando'

for caracter in nome:
    print(f'Letras do nome {nome}: {caracter}')

print('')
#--------------------------------------

clientes = [
    ('Fernando', 'xxx', 'xxx@email.com'), 
    ('Brunna', 'yyy', 'yyy@email.com')
    ]

for cliente in clientes:
    
    nome = cliente[0]
    cpf = cliente[1]
    email = cliente[2]

    print(f'Nome: {nome} \nCPF: {cpf} \nE-mail: {email} \n')

for cliente in clientes:
    
    nome, cpf, email = cliente

    print(f'Nome: {nome} \nCPF: {cpf} \nE-mail: {email} \n')