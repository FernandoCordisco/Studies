import random

def gerar_baralho(n_copias=2, coringas = True, embaralhado = True):
    baralho = list()
    naipes = ['♣️', '♦️', '♥️', '♠️']
    numeros = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']  

    for _ in range(n_copias):
        for naipe in naipes:
            for numero in numeros:
                carta = numero + naipe
                baralho.append(carta)
        
        if coringas:
            baralho.extend(['JK1', 'JK2', 'JK3', 'JK4'])

    if embaralhado:
        random.shuffle(baralho)

    return baralho

def mostrar_baralho(baralho):
    tamanho_baralho = len(baralho)
    print(f'Há {tamanho_baralho} cartas no baralho')
    print('Cartas:')
    print(' - '.join(baralho))
    print('')

def dar_as_cartas(baralho, n_jogadores = 4, n_cartas = 5):
    jogadores = dict()

    for i in range(n_jogadores):
        mao = list()
        while len(mao) < n_cartas:
            carta = baralho.pop(0)
            mao.append(carta)
        
        nome_jogador = f'Jogador {i+1}'
        jogadores[nome_jogador] = mao

    return jogadores

def mostrar_jogadores(jogadores):
    for jogador, mao in jogadores.items():
        print(f'Há {len(mao)} cartas na mão do {jogador}')
        print('Cartas:')
        for carta in mao:
            print(f'->{carta}')
        print('')

baralho = gerar_baralho()

mostrar_baralho(baralho)

jogadores = dar_as_cartas(baralho)

mostrar_baralho(baralho)

mostrar_jogadores(jogadores)