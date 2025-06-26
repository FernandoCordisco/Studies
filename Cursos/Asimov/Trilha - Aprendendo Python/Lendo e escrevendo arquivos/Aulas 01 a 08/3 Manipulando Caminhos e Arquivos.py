from pathlib import Path
import os

print(Path.cwd())
print(Path.cwd().is_absolute())

print(Path('primeira_pasta'))
print(Path('primeira_pasta').is_absolute())

print(Path.cwd() / 'primeira_pasta')
print((Path.cwd() / 'primeira_pasta').exists())

os.chdir(Path.home())
print(Path.cwd() / 'primeira_pasta')
print((Path.cwd() / 'primeira_pasta').exists())

print(__file__)
#caminho absoluto:
print(Path(__file__))
print(Path(__file__).is_absolute())
print(Path(__file__).parent / 'primeira_pasta')
print((Path(__file__).parent / 'primeira_pasta').exists())

caminho_arquivo = Path(__file__)
print(caminho_arquivo)
print(caminho_arquivo.anchor)
print(caminho_arquivo.name)
print(caminho_arquivo.stem)
print(caminho_arquivo.suffix)
print(caminho_arquivo.drive)
print(caminho_arquivo.parent)
print(caminho_arquivo.parents[0])
print(caminho_arquivo.parents[1])
print(caminho_arquivo.parents[2])