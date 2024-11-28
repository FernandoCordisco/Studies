import os

carros= [
('Fiat Uno', 80),
('Volkswagen Gol', 90),
('Chevrolet Onix', 100),
('Ford Ka', 95),
('Renault Sandero', 110),
('Hyundai HB20', 105),
('Toyota Corolla', 180),
('Honda Civic', 190),
('Jeep Renegade', 200),
('Chevrolet Tracker', 210),
]

alugados = []




def mostrar_lista_de_carros(lista_de_carros):
    for i, car in enumerate(lista_de_carros):
        print('[{}] - {} - {} /dia.' .format(i, car[0], car[1]))


while True:
    os.system('clear')
    print(f'\n' + '='*20 + '\n')
    print('Bem vindo a locadora de carro')
    print(f'\n' + '='*20 + '\n')
    print('O que deseja fazer?')
    print('0 - Mostrar o portifólio | 1 - Alugar um carro | 2 - Devolver um carro')
    op = int(input(""))

    os.system('clear')

    if op == 0:
        mostrar_lista_de_carros(carros)

    elif op == 1:
        mostrar_lista_de_carros(carros)
        print(f'\n' + '='*20 + '\n')
        cod_carro = int(input(f'Escolha o código do carro:\n'))
        dias = int(input(f'\nPor quantos dias deseja alugar o carro?\n'))
        os.system('clear')

        print('Você escolheu o carro {} por {} dias.'.format(carros[cod_carro][0], dias))
        print('O aluguel totalizaria em R$ {}. Deseja alugar?'.format(dias * carros[cod_carro][1]))

        conf = int(input(f'0 - Sim | 1 - Não\n'))

        if conf == 0:
            os.system('clear')
            print('Parabéns, você alugou o carro {} por {} dias.'.format(carros[cod_carro][0], dias))
            alugados.append(carros.pop(cod_carro))

    elif op == 2:
        if len(alugados) == 0:
            print('Não há carros para devolver.')

        else:
            print('Segue a lista de carros alugados. Qual você deseja devolver?')
            mostrar_lista_de_carros(alugados)
            cod_carro = int(input(f'Escolha o código do carro:\n'))

            os.system('clear')
            print('Obrigado por devolver o carro {}.'.format(alugados[cod_carro][0]))
            carros.append(alugados.pop(cod_carro))
    
    
    
    print(f'\n' + '='*20 + '\n')
    print('0 - Continuar | 1 - Sair')
    if int(input()) == 1:
        break