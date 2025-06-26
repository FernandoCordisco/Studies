# and / or / not
print('-----INÍCIO-----\n')

print('Digite "s" para "sim" e "n" para "não"\n')

resposta_fome = input('Estou com fome? ') == 's'
resposta_comida = input('Tenho comida? ') == 's'

print('')

if resposta_fome and not resposta_comida:
    print('Ir ao mercado')
    print('Voltar para casa')
    print('Preparar uma refeição')
    print('Comer a comida')

elif resposta_fome and resposta_comida:
    print('Preparar uma refeição')
    print('Comer a comida')

print('')
print('-----FIM-----')