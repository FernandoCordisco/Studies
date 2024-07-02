print('-----INÍCIO-----\n')

print('Digite "s" para "sim" e "n" para "não"\n')

resposta_fome = input('Está com fome? \nDigite sua resposta: ')

if resposta_fome == 's':
    resposta_comida = input('Tem comida em casa? \nDigite sua resposta: ')

    if resposta_comida == 's':
        print('Preparar uma refeição')
        print('Comer a comida')
    
    elif resposta_comida == 'n':
        print('Ir ao mercado')
        print('Voltar para casa')
        print('Preparar uma refeição')
        print('Comer a comida')

    else:
        print('Resposta inválida')
        
    print('-----FIM-----\n')
elif resposta_fome == 'n':
    print('-----FIM-----\n')

else:
    print('Resposta inválida')
    print('-----FIM-----\n')

