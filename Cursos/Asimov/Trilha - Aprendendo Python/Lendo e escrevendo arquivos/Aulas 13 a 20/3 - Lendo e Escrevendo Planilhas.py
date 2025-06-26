import pandas as pd
from pathlib import Path

pasta_atul =  Path(__file__).parent

#Lendo tabelas com DataFrame
'''
tabela_clientes = pd.read_excel(pasta_atul / 'planilhas' / "clientes.xlsx")
print(tabela_clientes.head())
'''

#Lendo aba específica
'''
tabela_clientes = pd.read_excel(pasta_atul / 'planilhas' / "clientes.xlsx", sheet_name='SC')
print(tabela_clientes.head())
'''

#Modificando header
'''
tabela_clientes = pd.read_excel(pasta_atul / 'planilhas' / 'clientes.xlsx', header=1)
print(tabela_clientes.head(10))
'''

#Adicionando coluna de index
'''
tabela_clientes = pd.read_excel(pasta_atul / 'planilhas' / 'clientes.xlsx', header=0, index_col=0)
print(tabela_clientes.head(10))
'''

#Lendo colunas específicas
'''
tabela_clientes = pd.read_excel(pasta_atul / 'planilhas' / 'clientes.xlsx', index_col=0, usecols=(0,1))
#usecols='A:B'
print(tabela_clientes.head(10))
'''

#Casas deciamais e thousands
'''
tabela_clientes = pd.read_excel(pasta_atul / 'planilhas' / 'clientes.xlsx', index_col=0, decimal='.')
print(tabela_clientes.head(10))

tabela_clientes = pd.read_excel(pasta_atul / 'planilhas' / 'clientes.xlsx', index_col=0, thousands='.')
print(tabela_clientes.head(10))'
'''

#Escrevendo planilha
'''
tabela_clientes = pd.read_excel(pasta_atul / 'planilhas' / 'clientes.xlsx')
tabela_clientes.to_excel(pasta_atul / 'planilhas' / 'copia_clientes.xlsx')
'''
#Escrevendo planilha com diversas abas

tabela_clientes_rs = pd.read_excel(pasta_atul / 'planilhas' / 'clientes.xlsx', sheet_name='RS')
tabela_clientes_sc = pd.read_excel(pasta_atul / 'planilhas' / 'clientes.xlsx', sheet_name='RS')

with pd.ExcelWriter(pasta_atul / 'planilhas' / 'copia_clientes.xlsx') as nova_planilha:
    tabela_clientes_rs.to_excel(nova_planilha, sheet_name='RS', index=False)
    tabela_clientes_sc.to_excel(nova_planilha, sheet_name='SC', index=False)