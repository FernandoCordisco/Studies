from pathlib import Path

pasta_atual = Path(__file__).parent

# Lendo um arquivo (forma não recomendada)
'''
lista_compras = open(pasta_atual / 'Lista_de_compras.txt')
print(lista_compras.read())
lista_compras.close()
'''

# Lendo um arquivo (forma recomendada)
'''
with open(pasta_atual / 'Lista_de_compras.txt') as lista_compras:
    print(lista_compras.read())
'''

# Lendo linha a linha
'''
with open(pasta_atual / 'Lista_de_compras.txt') as lista_compras:
    linha = lista_compras.readline()
    while linha != '':
        print(linha, end='')
        linha = lista_compras.readline()
'''

# Lendo todas as linhas
'''
with open(pasta_atual / 'Lista_de_compras.txt') as lista_compras:
    print(lista_compras.readlines())
'''
# Escrevendo um arquivo 
'''
itens_ja_comprados = ['farinha', 'fermento', 'agua']

with open(pasta_atual / 'Lista_de_compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

with open(pasta_atual / 'Lista_de_compras_atualizada.txt', mode='w') as lista_atualizada:
    for item in itens_lista:
        if not item.replace('\n', '') in itens_ja_comprados:
            lista_atualizada.write(item)
'''

# Escrevendo linha a linha
'''
itens_ja_comprados = ['farinha', 'fermento', 'agua']

with open(pasta_atual / 'Lista_de_compras.txt') as lista_compras:
    itens_lista = lista_compras.readlines()

itens_lista_atualizada = list()
for item in itens_lista:
    if not item.replace('\n', '') in itens_ja_comprados:
        itens_lista_atualizada.append(item)

with open(pasta_atual / 'lista_de_compras_atualizada.txt', mode='w') as lista_atualizada:
    itens_lista_atualizada[-1] = itens_lista_atualizada[-1].replace('\n', '') 
    lista_atualizada.writelines(itens_lista_atualizada)
'''

# Acrescentando valores a lista

novos_itens = ['banana']
novos_itens_c_quebra = [f'\n{item}' for item in novos_itens]
'''for item in novos_itens:
    novos_itens_c_quebra.append(f'\n{item}')'''

with open(pasta_atual / 'Lista_de_compras.txt', mode='a') as lista_adicionada:
    lista_adicionada.writelines(novos_itens_c_quebra)