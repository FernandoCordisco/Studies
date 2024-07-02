capitais = {
    'Brasil': 'Brasilia',
    'França': 'Paris',
    'Japão': 'Tóquio'
    }

print('Brasil' in capitais)
print('Inglaterra' in capitais)

print('')

pais = 'Inglaterra'

if pais in capitais:
    capital = capitais[pais]
    print(f'A capital do país {pais} é {capital}.')
else:
    print(f'Não há registro do país {pais}.')

#-----------------

print('')

texto = 'Eu estudo Python'

print('Eu' in texto)
print('ESTUDO' in texto)
print('estudo Py' in texto)
