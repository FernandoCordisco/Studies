print(f'----- ÍNICIO -----\n')

estados = {
    "Acre": "rio branco",
    "Alagoas": "maceió",
    "Amapá": "macapá",
    "Amazonas": "manaus",
    "Bahia": "salvador",
    "Ceará": "fortaleza",
    "Distrito Federal": "brasília",
    "Espírito Santo": "vitória",
    "Goiás": "goiânia",
    "Maranhão": "são luís",
    "Mato Grosso": "cuiabá",
    "Mato Grosso do Sul": "campo grande",
    "Minas Gerais": "belo horizonte",
    "Pará": "belém",
    "Paraíba": "joão pessoa",
    "Pernambuco": "recife",
    "Piauí": "teresina",
    "Paraná": "curitiba",
    "Rio de Janeiro": "rio de janeiro",
    "Rio Grande do Norte": "natal",
    "Rio Grande do Sul": "porto alegre",
    "Rondônia": "porto velho",
    "Roraima": "boa vista",
    "Santa Catarina": "florianópolis",
    "São Paulo": "são paulo",
    "Sergipe": "aracaju",
    "Tocantins": "palmas"
}

pontuacao = 0
n = 0
capitais = list(estados.values())

print(f'Caso queira para o jogo, digite "q" \n')
for estado in estados:
    
    resposta_capital = input(f'Qual o capital de / do {estado}? \nResposta: ') 
    
    resposta_capital = resposta_capital.lower()

    if resposta_capital == 'q':
        break
    if capitais[n] == resposta_capital:
        print(f'Acertou\n') 
        pontuacao += 1
    else:
        print('errou')
        print(f'A resposta correta era: {capitais[n]}! \n')
    n += 1

porcertagem = (100 * pontuacao) / (n)

print('')
print(f'Acerto: {pontuacao} de {n} / {porcertagem:.2f}%')


print('')
print('----- FIM -----')
    