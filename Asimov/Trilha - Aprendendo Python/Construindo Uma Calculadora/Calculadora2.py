import os

print('===========')
operations = {
    '+': 'Soma',
    '-': 'Subtração',
    '*': 'Multiplicação',
    '/': 'Divisão',
    '^': 'Exponenciação'
}

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    i = 0
    for op, name in operations.items():
        print(i, ":", name)
        i += 1
    print(f'\nEscolha uma operação que deseja utilizar:')
    op = int(input())
    op_string = list(operations.keys())[op]

    print(f'\n{op_string} escolhida.')
    print(f'\nQual o primeiro valor?')
    v1 = float(input())
    print(f'Qual o segundo valor?')
    v2 = float(input())

    if op == 0:
        result = v1 + v2
    elif op == 1:
        result = v1 - v2
    elif op == 2:
        result = v1 * v2
    elif op == 3:
        result = v1 / v2
    elif op == 4:
        result = v1 ** v2

    print(f'{v1} {op_string} {v2} = {result}' )
    print('\nDeseja fazer mais alguma operação? (Digite 1 para sair)')
    comando = int(input())

    if comando == 1:
        break