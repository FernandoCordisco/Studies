produtos = {
    'Banana': 3.60,
    'Maçã': 2.50,
    'Amora': 1.40,
    'Melancia': 10.20
}

print(produtos)

print(produtos.get('Banana', 'Não foi encontrado'))
print(produtos.get('Laranja', 'Não foi encontrado'))

produtos.setdefault('Laranja', 5.20)

print(produtos)

for produto in produtos.keys():
    print(produto)

for valor in produtos.values():
    print(valor)

for par in produtos.items():
    print(par)

for k, v in produtos.items():
    print(f'{k} --> {v}')

novos_produtos = {
    'Pera': 3.25,
    'Banana': 8.00
}

produtos.update(novos_produtos)

print(produtos)

produtos_copia = produtos.copy()


produtos.clear()