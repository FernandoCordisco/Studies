alfabeto_mi = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
            ]

alfabeto_ma = ['A', 'B', 'C','D', 'E', 'F', 'G', 'H', 'I',
            'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
            'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
            ]

palavra_cifra = list()
palavra = input('Digite uma palavra: ')
chave = int(input('Digite um número: '))

def cifrar_caractere(alfabeto, chave, letra):
    posicao_alfabeto = int(alfabeto.index(letra))
    chave_nova = posicao_alfabeto + chave

    while chave_nova >= len(alfabeto):
        chave_nova = chave_nova - len(alfabeto)
    
    while chave_nova < 0:
        chave_nova = chave_nova + len(alfabeto)

    cifra = alfabeto[chave_nova]
    return palavra_cifra.append(cifra)

for letra in palavra:

    if letra in alfabeto_mi:

        cifrar_caractere(alfabeto_mi, chave, letra)

    elif letra in alfabeto_ma:

        cifrar_caractere(alfabeto_ma, chave, letra)

    else:
        palavra_cifra.append(letra)

print(f'A palavra {palavra} com chave de {chave} na Cifra de césar fica: ' + ''.join(palavra_cifra))
    
