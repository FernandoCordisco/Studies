from pathlib import Path

caminho = Path('primeira_pasta/segunda_pasta')
caminho2 = Path('/home/leng/Documentos/Studies/Asimov/Trilha - Aprendendo Python/Lendo e escrevendo arquivos/Aulas 01 a 08/')

print(caminho)
print(type(caminho))
print(caminho2)

for nome in ['arquivo1.txt', 'arquivo2.txt', 'arquivo3.txt']:
    caminho_arquivo = caminho / nome
    print(caminho_arquivo)

print(Path.home() / 'Documents' / 'Etc')