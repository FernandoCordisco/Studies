capitais = {
    'Brasil': 'Brasilia',
    'França': 'Paris',
    'Japão': 'Tóquio'
    }

print(capitais['Brasil'])

for pais in capitais:
    capital = capitais[pais]
    print(f'A capital de {pais} é {capital}')

d = dict()

d[10] = 'abc'
d['CHAVE'] = 5
d[3.15] = True

print(d)