#Variáveis
carros = [
['Fiat Uno', '80'],
['Volkswagen Gol', '90'],
['Chevrolet Onix', '100'],
['Ford Ka', '95'],
['Renault Sandero', '110'],
['Hyundai HB20', '105'],
['Toyota Corolla', '180'],
['Honda Civic', '190'],
['Jeep Renegade', '200'],
['Chevrolet Tracker', '210'],
]

resposta = int()
loop = bool()

#Funções
def mostrar_carros(carros):
    print('----- CARROS DISPONÍVEIS -----')
    n = 0 
    for carro, valor in carros:
        print(f"[{n}] -> {carro} - R$ {valor} por dia.")
        n+=1
    
def home(resposta, loop):
    print('-'*50)
    print('Bem vindo a locadora de carros!')
    print('-'*50)
    print('')
    print('O que deseja fazer?\n')
    print(f'0 -> Mostrar portifólio | 1 -> Alugar um carro | 2 -> Devolver um carro')
    
    opcoes = '0-1-2'
    loop = True
    while loop:

        resposta = input('Resposta: ')
        print('')
        if resposta in opcoes:
            loop = False

    if resposta == '0':
        portifolio(resposta, loop)
'''    
    elif resposta == '1':
        alugar_carro()

    elif resposta == '2':
        devolver_carro()
'''

def portifolio(resposta, loop):
    print('-'*50)
    mostrar_carros(carros)
    print('-'*50) 
    print('')
    print('0 -> CONTINUAR | 1 -> SAIR')

    opcoes = '0-1'
    loop = True

    while loop:
        resposta = input('Resposta: ')
        print('')
        if resposta in opcoes:
            loop = False

    if resposta == '0':
        home(resposta, loop)

    elif resposta == '1':
        pass

    
def alugar_carro():
    print('-'*50)
    mostrar_carros(carros)
    print('-'*50) 
    print('')
    print('Escolha o código do carro')

#def devolver_carro():


home(resposta, loop)