import pickle
from pathlib import Path

pasta_atual = Path(__file__).parent

#Salvando arquivos pickle
'''
minha_lista = [0, 1, 2]
meu_dict = {'a': 1, 'b': 2}

with open(pasta_atual / 'pickles' / 'minha_lista.pickle', 'wb') as f:
    pickle.dump(minha_lista, f)

with open(pasta_atual / 'pickles' / 'meu_dict.pickle', 'wb') as f:
    pickle.dump(meu_dict, f)

#Lendo arquivos pickle

with open(pasta_atual / 'pickles' / 'minha_lista.pickle', 'rb') as f:
    minha_lista_lida = pickle.load(f)

with open(pasta_atual / 'pickles' / 'meu_dict.pickle', 'rb') as f:
    meu_dict_lida = pickle.load(f)

print(minha_lista)
print(type(minha_lista))
print(meu_dict)
print(type(meu_dict))
'''

#Salvando a instância de uma classe com pickle

class Pessoa:
    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def quem_sou_eu(self):
        print(f'Eu sou {self.nome} e tenho {self.idade} anos.')

'''
inst_joao = Pessoa('Joao', 31)
inst_joao.quem_sou_eu()

with open(pasta_atual / 'pickles' / 'inst_joao.pickle', 'wb') as f:
    pickle.dump(inst_joao, f)
'''
#Lendo a mesma instância:

with open(pasta_atual / 'pickles' / 'inst_joao.pickle', 'rb') as f:
    inst_joao_lida = pickle.load(f)

inst_joao_lida.quem_sou_eu()