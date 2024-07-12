from ModuloA.Script_A import var_a
from ModuloB.Script_B import var_b
from ModuloC.Script_C import var_c

def func():
    print(var_a + var_b + var_c)


if __name__ == '__main__':
    print('Testando: func')
    func()