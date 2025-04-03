import pandas as pd
from pathlib import Path

pasta_atul = Path(__file__).parent
pasta_consilidada = pasta_atul / 'planilhas' / 'planilha_consolidada'
pasta_separadas = pasta_atul / 'planilhas' / 'planilhas_separadas'
caminho_planilha = pasta_atul / 'planilhas' / 'clientes.xlsx'
abas = pd.ExcelFile(caminho_planilha).sheet_names


def separando_planilhas():

    for aba in abas:
        tabela_clientes = pd.read_excel(caminho_planilha, sheet_name=aba)
        tabela_clientes.to_excel(pasta_separadas / f'clientes_{aba}.xlsx', sheet_name=aba, index=False)

def consolidando_planilhas():

    
    with pd.ExcelWriter(pasta_consilidada / 'clientes_consolidada.xlsx') as tabela_consolidada:
        for aba in abas:
            tabela_clientes = pd.read_excel(pasta_separadas / f'clientes_{aba}.xlsx', sheet_name=aba)
            tabela_clientes.to_excel(tabela_consolidada, sheet_name=aba, index=False)

separando_planilhas()
consolidando_planilhas()
