from pathlib import Path
import shutil
import os

# Criando pasta
'''
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino6'
caminho_pasta_destino.mkdir(exist_ok=True)
'''
# Criando pasta com todas as pastas anterioes necessárias
'''
pasta_atual = Path(__file__).parent
caminho_pasta_destino = pasta_atual / 'destino7' / 'destino7.1'
caminho_pasta_destino.mkdir(parents=True)
'''
# Copiando pastas
'''
pasta_atual = Path(__file__).parent
shutil.copytree(pasta_atual / 'destino5', pasta_atual / 'destino1' / 'destino5')

'''
# Deletando pastas vazias
'''
pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino7' / 'destino7.1'
pasta_remover.rmdir()
'''
# Deletando pastas com conteúdo

pasta_atual = Path(__file__).parent
pasta_remover = pasta_atual / 'destino1' / 'destino5'
shutil.rmtree(pasta_remover)