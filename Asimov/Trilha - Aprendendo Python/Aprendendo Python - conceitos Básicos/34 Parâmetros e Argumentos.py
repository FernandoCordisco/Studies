def somar_dois(n):
    return n + 2

x = 10 

resultado = somar_dois(x)

print(resultado)

def adicionar_final(texto, filial="!!!!"):
    return texto + filial

print(adicionar_final('Olá', '!'))
print(adicionar_final('Olá'))

def dividir (a,b):
    if b == 0:
        return 'Impossível dividir'
    return a / b

print(dividir(a = 10, b = 0))
print(dividir(b = 10, a = 0))

def dizer_ola():
    print('olá')

dizer_ola()