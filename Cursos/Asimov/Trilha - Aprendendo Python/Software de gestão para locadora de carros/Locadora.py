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

carros_alugados = list()

#Funções
def mostrar_carros(carros):
    print('----- CARROS DISPONÍVEIS -----')
    n = 0 
    for carro, valor in carros:
        print(f"[{n}] -> {carro} - R$ {valor} por dia.")
        n+=1

def respostas(opcoes):

    loop = True
    while loop:

        resposta = int(input('Resposta: '))
        print('')
        if resposta in opcoes:
            loop = False
    
    return resposta

def home():
    print('-'*50)
    print('Bem vindo a locadora de carros!')
    print('-'*50)
    print(f'\nO que deseja fazer?\n')
    print(f'0 -> Mostrar portifólio | 1 -> Alugar um carro | 2 -> Devolver um carro')
    
    resposta = respostas([0,1,2])

    if resposta == 0:
        portifolio()

    elif resposta == 1:
        alugar_carro(carros, carros_alugados)


    elif resposta == 2:
        devolver_carro(carros_alugados)


def portifolio():
    print('-'*50)
    mostrar_carros(carros)
    print('-'*50) 
    print(f'\n0 -> CONTINUAR | 1 -> SAIR')

    resposta = respostas([0, 1])

    if resposta == 0:
        home()

    elif resposta == 1:
        pass

    
def alugar_carro(carros, carros_alugados):
    print('-'*50)
    mostrar_carros(carros)
    print('-'*50) 
    print(f'\nEscolha o código do carro para alugar:')
    
    opcoes = list()
    n = 0
    for _ in carros:
        opcoes.append(n)
        n +=1

    resposta1 = respostas(opcoes) 
    
    carro_selecionado = carros.pop(resposta1)
    carro = carro_selecionado[0]
    valor = int(carro_selecionado[1])

    dias_alugado = int(input(f'Quantos dias deseja alugar o carro? \nResposta: '))

    valor_total = float(valor * dias_alugado)

    print(f'\nVocê deseja alugar o carro {carro}, por {dias_alugado} dias no valor de R$ {valor_total:.2f}?')

    print('\nDeseja alugar? - 0 -> SIM | 1 -> NÃO')
    resposta = respostas([0, 1])

    if resposta == 0:
        carros_alugados.append([carro, valor ,valor_total])
        carro_selecionado.clear()
        home()

    if resposta == 1:
        carros.insert(resposta1,[carro, valor])
        carro_selecionado.clear()
        home()

def devolver_carro(carros_alugados):
    print('----- CARROS ALUGADOS -----')
    n = 0 
    for carro, valor, valor_total in carros_alugados:
        print(f"[{n}] -> {carro} - R$ {valor_total}.")
        n+=1

    print(f'\nEscolha o código do carro para devolver:')

    if not carros_alugados:
        print(f'\nSem carros para devolução!\n')
    else:
           
        opcoes = list()
        n = 0
        for _ in carros_alugados:
            opcoes.append(n)
            n +=1

        resposta = respostas(opcoes) 

        carro_selecionado = carros_alugados.pop(resposta)
        carro = carro_selecionado[0]
        valor = int(carro_selecionado[1])
        carros.append([carro, valor])
        carro_selecionado.clear()
        
    home()

#Main

home()