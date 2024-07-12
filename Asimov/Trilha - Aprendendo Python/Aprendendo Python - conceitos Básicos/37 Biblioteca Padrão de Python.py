import math
import datetime
import random
import os
import time

inicio = time.time()

print(math.pi)

print(math.log(16, 2))

print('')

agora = datetime.datetime.now()

ano_2000 = datetime.datetime(2000,1,1)

print(agora - ano_2000)

print('')

for _ in range(5):
    n = random.randint(1, 10)
    print(f'Número escolhido: {n}')

nomes = ['Brunna', 'Brenno', 'Piter']

for _ in range(5):
    nome = random.choice(nomes)
    print(f'Nome escolhido: {nome}')

print('')

print(os.getcwd())
print(os.listdir())

print('')

print('Primeira linha')

time.sleep(5)

print('Segunda linha')

final = time.time()

tempo_execucao = final - inicio

print(f'O tempo de execução do programa foi de {tempo_execucao:.3f}s.')