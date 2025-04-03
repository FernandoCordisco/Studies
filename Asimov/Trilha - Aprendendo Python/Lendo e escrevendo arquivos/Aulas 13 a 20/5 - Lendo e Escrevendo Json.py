import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
pasta_atual = Path(__file__).parent

data_json = '''
{
  "assinantes": [
    {
      "nome": "Adriano Soares",
      "telefone": "51 99999999",
      "email": "adriano@email.com",
      "em_dia": true
    },
    {
      "nome": "Juliano faccioni",
      "telefone": "51 99999999",
      "email": "juliano@email.com",
      "em_dia": false
    }
  ],
  "data_extração": "2023/08/22"
}
'''

#Convertendo json para dicionário
'''
dado_convertido = json.loads(data_json)
'''

#Convertendo para Json
'''
dado_desconvertido = json.dumps(dado_convertido, ensure_ascii=False, indent=2)

print(dado_convertido)
print(dado_desconvertido)
'''

#Lendo arquivos json
'''
with open(pasta_atual / 'jsons' / 'assinantes.json') as f:
    dado_carregado = (json.load(f))
    print(dado_carregado)
    print(type(dado_carregado))
'''

#Escrevendo arquivos json

with open(pasta_atual / 'jsons' / 'assinantes.json') as f:
    dado_carregado = (json.load(f))

with open(pasta_atual / 'jsons' / 'assinantes_copia.json', 'w') as f:
    json.dump(dado_carregado, f, indent=2, ensure_ascii=False)
