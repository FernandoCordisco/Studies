usuario = 'adm'
senha = 'adm123'

print('-----INÍCIO-----\n')

usuario_input = input('Qual o usuário? \nDigite aqui:') == usuario
print('')
senha_input = input('Qual a senha? \nDigite aqui:') == senha

print('')

if usuario_input and senha_input:
    print(f'Acesso liberado, seja bem-vindo, usuário {usuario}!')

elif usuario_input and not senha_input:
    print('Senha inválida.')

elif not usuario_input and senha_input:
    print('Usuário não encontrado.')

else:
    print('Usuário e senha inválidos.')

print('')
print('-----FIM-----')