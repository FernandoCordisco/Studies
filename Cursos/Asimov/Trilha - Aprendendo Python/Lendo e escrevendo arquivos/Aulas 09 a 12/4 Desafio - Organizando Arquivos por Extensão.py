from pathlib import Path
import shutil
import os

pasta_atual = Path(__file__).parent
pasta_a_organizar = pasta_atual / 'arquivos_desafio'
pasta_organizacao = pasta_atual / 'arquivos_desafio_organizado'

# Criando a pasta

if pasta_organizacao.exists():
    shutil.rmtree(pasta_organizacao)

pasta_organizacao.mkdir()

# Criando Backup 

shutil.make_archive(pasta_organizacao / 'backup', 'zip', pasta_a_organizar)

# Criando pasta por extensão 

def listando_extensao(pasta_a_organizar):
    extensoes = list()
    for arquivo in  os.listdir(pasta_a_organizar):
        nome, extensao_do_arquivo = os.path.splitext(arquivo)
        
        if extensao_do_arquivo not in extensoes:
            extensoes.append(extensao_do_arquivo)

    return extensoes

extensoes = listando_extensao(pasta_a_organizar)

# Criando pasta e copiando o arquivo 

def criacao_de_pasta_e_copia():

    for extensao in extensoes:
        pasta_por_extensao = pasta_organizacao/ extensao[1:]
        pasta_por_extensao.mkdir()
        
        for arquivo in  os.listdir(pasta_a_organizar):
            nome, extensao_do_arquivo = os.path.splitext(arquivo)
            if extensao_do_arquivo in extensao:
                caminho = pasta_a_organizar / arquivo
                destino = pasta_por_extensao / arquivo
                shutil.copyfile(caminho, destino)
        
criacao_de_pasta_e_copia()

