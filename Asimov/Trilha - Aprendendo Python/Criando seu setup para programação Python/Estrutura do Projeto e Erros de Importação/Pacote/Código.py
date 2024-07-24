from Pacote.ModuloA.Script_A import var_a
from Pacote.ModuloB.Script_B import var_b
from Pacote.ModuloC.Script_C import var_c

def func():
    print(var_a + var_b + var_c)


if __name__ == '__main__':
    print('Testando: func')
    func()