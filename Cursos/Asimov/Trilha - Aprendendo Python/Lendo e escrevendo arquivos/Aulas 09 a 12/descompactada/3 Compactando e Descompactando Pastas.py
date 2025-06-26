from pathlib import Path
import shutil

# Compactando arquivos
pasta_atual = Path(__file__).parent
pasta_a_ser_compactado = pasta_atual
nome_arquivo = pasta_atual / 'compactado'
shutil.make_archive(nome_arquivo, 'zip', pasta_a_ser_compactado)