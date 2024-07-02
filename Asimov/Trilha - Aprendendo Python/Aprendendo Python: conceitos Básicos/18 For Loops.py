for n in range(5):
    print(f'O valor de N é {n}')

for _ in range(2):
    print('Olá!')


#-----------------------

print('-----INÍCIO-----\n')

numero_secreto = 10 
descobriu = False

for _ in range(3):

    if not descobriu:
        chute = int(input('Chute um número: ')) 
        if chute > numero_secreto:
            print('O valor informado é maior.')
        elif chute < numero_secreto:
            print('O valor informado é menor')
        else:
            descobriu = True


print('')

if descobriu:
    print(f'Parabéns, você acertou. O número secreto era: {numero_secreto}')
else:
    print(f'Que pena, você não acertou. O número secreto era: {numero_secreto}')


print('')
print('-----FIM-----')