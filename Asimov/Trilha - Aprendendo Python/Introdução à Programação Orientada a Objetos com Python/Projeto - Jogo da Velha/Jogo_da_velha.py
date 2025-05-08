import random
import os

posicoes = [i for i in range(1,10)]
posicoes_ja_selecionada = []
peca = 'X'
peca2 = 'O'

continuar = 1
def mostrar_jogo():
    a, b, c = 0, 1, 2
    for i in range(3):
        print(f'{posicoes[a]} - {posicoes[b]} - {posicoes[c]}')
        a += 3
        b += 3
        c += 3

def selecionar_posicao():
    posicao_escolhida = int(input('Selecione a posição: ')) - 1
    if posicao_escolhida in posicoes_ja_selecionada:
        print('Posição já está em uso, seleciona outra.')
        selecionar_posicao()
    else:
        posicoes[posicao_escolhida] = peca
        posicoes_ja_selecionada.append(posicao_escolhida)

def maquina_joga():
    posicoes_disponiveis = [i for i in range(9) if i not in posicoes_ja_selecionada]
    posicao_escolhida = random.choice(posicoes_disponiveis)
    posicoes[posicao_escolhida] = peca2
    posicoes_ja_selecionada.append(posicao_escolhida)

def validar_jogo():
    combinacoes = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    
    for a, b, c in combinacoes:
        if posicoes[a] == posicoes[b] == posicoes[c]:
            mostrar_jogo()
            if posicoes[a] == 'X':
                print('Vitória do jogador!')
            else: 
                print('Vitória da máquina!')
            return True
        
    if len(posicoes_ja_selecionada) == 9:
            print("Empate!")
            return True
    
def jogo_da_velha():
    while True:
        os.system('cls')
        print('=====JOGO DA VELHA=====')
        mostrar_jogo()
        selecionar_posicao()
        if validar_jogo():
            break
        maquina_joga()
        if validar_jogo():
            break
        
jogo_da_velha()