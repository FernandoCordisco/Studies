#metodos de números
x = 4.5

print(x.as_integer_ratio())

print(x.is_integer())

#Metodos de String

palavra = 'Olá MuNdo'

print(palavra.upper())
print(palavra.lower())

Arquivo = '2023_01_01_NotaFiscal.pdf'

print(Arquivo.endswith('.pdf'))
print(Arquivo.startswith('2023'))

if Arquivo.startswith('2023') and Arquivo.endswith('.pdf'):
    print(f'{Arquivo} é um arquivo válido')

texto = 'Hoje em dia todo dia é um novo dia. mais um dia chega. Dia'

print(texto.count('a'))
print(texto.count('dia'))
print(texto.lower().count('dia'))

seq = 'aaaaaaabaaaaabaaaabaaaa'

print(seq.find('b'))
print(seq.index('b'))
print(seq.find('c'))
# print(seq.index('c')) - Apresenta erro

print(seq[seq.find('b'):])

s1 = '41584561564'

print(s1.isdigit())

s2 = 'anajfnjnJAnbjhjnAj'

print(s2.isalpha())

s3 = '1s5g456as45s4g5a64'

print(s3.isdigit())
print(s3.isalpha())

frase = 'Estou estudando Python!'

print(frase.replace('!', '?'))

linha = 'Item1          Item2         Item2'
print(linha.split())

linha = 'Item1; Item2; Item2'
print(linha.split(';'))

nomes = ['Fernando', 'Letícia', 'Ana' ]
print(' ------ '.join(nomes))
