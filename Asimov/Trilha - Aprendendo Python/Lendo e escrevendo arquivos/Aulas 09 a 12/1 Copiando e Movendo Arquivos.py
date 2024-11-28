from pathlib import Path
import shutil
import os

# Copiando arquivo com copyfile
'''
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual / 'destino1' / 'texto.txt'

shutil.copyfile(caminho_arquivo,  caminho_arquivo_destino)
'''
# Copiando arquivo com copy (permissões iguais ao arquivo original)
'''
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino2'

shutil.copy(caminho_arquivo,  caminho_pasta_destino)
'''

# Copiando arquivo com copy2 (Copia metadados)
'''
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino3'

shutil.copy2(caminho_arquivo,  caminho_pasta_destino)
'''
# Movendo arquivos
'''
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_pasta_destino = pasta_atual / 'destino4'

shutil.move(caminho_arquivo, caminho_pasta_destino)
'''
# Ou
'''
pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual / 'destino4' / 'texto.txt'

shutil.move(caminho_arquivo, caminho_arquivo_destino)
'''
# Deletando arquivos

pasta_atual = Path(__file__).parent
caminho_arquivo = pasta_atual / 'texto.txt'
caminho_arquivo_destino = pasta_atual / 'destino5' / 'texto.txt'

if caminho_arquivo.exists():
    shutil.copyfile(caminho_arquivo, caminho_arquivo_destino)

    os.remove(caminho_arquivo)