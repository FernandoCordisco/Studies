#Baralho

import random

#variáveis cartas

naipes = ['♣️', '♦️', '♥️', '♠️']
numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
coringas = ['JK1', 'JK2', 'JK3', 'JK4']
baralho = list()

#Variáveis para gerar o baralho

opcao_coringa = True
opcao_quantidade_baralho = 2
opcao_embaralhado = True

#variáveis para dar as cartas

quantidade_jogadores = 5
carta_por_jogador = 5
cartas_do_jogador = list()
jogador_e_carta = dict()

#Funções

def gerar_baralho(op_coringa, op_quantidade, op_embaralhado):

    for naipe in naipes:

        n = 0

        while n < op_quantidade:

            for numero in numeros:
                baralho.append(numero + naipe)
        
            n += 1
    
    if op_coringa: 

        n = 0

        while n < op_quantidade:

            for coringa in coringas:
                baralho.append(coringa)

            n += 1

    if op_embaralhado:
        random.shuffle(baralho)

    return baralho


def mostrar_baralho(baralho):
    quantidade_cartas = len(baralho)

    print(f'O baralho possui {quantidade_cartas} cartas!\n')
    print('Essas são as cartas do baralho:')
    print(' - '.join(baralho))
    print('')


def dar_as_cartas(quantidade_jogadores, carta_por_jogador, baralho,cartas_do_jogador, jogador_e_carta):
    
    j = 1
    quantidade_cartas = quantidade_jogadores *  carta_por_jogador   
    cartas_sorteadas = random.sample(baralho, quantidade_cartas)
    
    for i in range(carta_por_jogador):
        comeco = int(i*quantidade_cartas/carta_por_jogador)
        final = int((i+1)*quantidade_cartas/carta_por_jogador)
        cartas_do_jogador.append(cartas_sorteadas[comeco:final])

    for cartas in cartas_do_jogador:
        jogador_e_carta.update({j: cartas})
        j += 1

    return jogador_e_carta

def mostrar_jogadores(jogador_e_carta):

    for jogador, cartas in jogador_e_carta.items():
        print(f'Jogador {jogador} recebe as cartas: ' + ' - '.join(cartas) + '.')


#main

gerar_baralho(opcao_coringa, opcao_quantidade_baralho, opcao_embaralhado)

mostrar_baralho(baralho)

dar_as_cartas(quantidade_jogadores, carta_por_jogador, baralho, cartas_do_jogador, jogador_e_carta)

mostrar_jogadores(jogador_e_carta)