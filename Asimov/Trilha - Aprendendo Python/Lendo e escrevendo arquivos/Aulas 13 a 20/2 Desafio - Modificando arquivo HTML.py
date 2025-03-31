from pathlib import Path
import pandas as pd

pasta_atual = Path(__file__).parent

tabela_clientes = pd.read_excel(pasta_atual / 'planilhas' / 'clientes.xlsx')
print(tabela_clientes.head(10))

