import os
import time
import sys

def informar_numero():
    n1 = float(input('Primeiro número: '))
    n2 = float(input('Segundo número: '))
    return(n1, n2)

def soma(n1, n2):
    soma = n1 + n2
    print(f'{n1} + {n2} = {soma}')

def subtracao(n1, n2):
    subtracao = n1 - n2
    print(f'{n1} - {n2} = {subtracao}')

def multiplicacao(n1, n2):
    multiplicacao = n1 * n2
    print(f'{n1} * {n2} = {multiplicacao}')

def divisao(n1, n2):
    divisao = n1 / n2
    print(f'{n1} / {n2} = {divisao}')

def exponenciacao(n1, n2):
    exponenciacao = pow(n1, n2)
    print(f'{n1} ^ {n2} = {exponenciacao}')

def escolha_de_operacao():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f'----CALCULADORA----\n')
    print('Escolha a operação desejada:')
    print(f'0 - Soma \n1 - Subttração \n2 - Multiplicação \n3 - Divisão \n4 - Exponenciação')
    escolha = str(input(f'\nOperação desejada: '))

    if escolha == '0':
        n1, n2 = informar_numero()
        soma(n1, n2)
        escolha_continuar()

    elif escolha == '1':
        n1, n2 = informar_numero()
        subtracao(n1, n2)
        escolha_continuar()

    elif escolha == '2':
        n1, n2 = informar_numero()
        multiplicacao(n1, n2)
        escolha_continuar()

    elif escolha == '3':
        n1, n2 = informar_numero()
        divisao(n1, n2)
        escolha_continuar()

    elif escolha == '4':
        n1, n2 = informar_numero()
        exponenciacao(n1, n2)
        escolha_continuar()

    else:
        print('Opção inválida. Escolha novamente.')
        time.sleep(2)
        escolha_de_operacao()

def escolha_continuar():
    escolha = str(input(f'\nDeseja continuar? \n0 - Sim | 1 - Não \n'))

    if escolha == '0':
        escolha_de_operacao()

    elif escolha == '1':
        sys.exit()
    
    else:
        print('Opção inválida. Escolha novamente.')
        escolha_continuar()

escolha_de_operacao()