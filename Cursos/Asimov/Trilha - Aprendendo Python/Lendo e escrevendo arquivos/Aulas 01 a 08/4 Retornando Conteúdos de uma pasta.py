from pathlib import Path
import os

# Listando arquivos de uma pasta
print(os.listdir(Path.home()))
print(list(Path.cwd().glob('*')))

# Listando arquivos de uma determinada extensão 
print(list(Path.cwd().glob('*.py')))

# Listar tudo dentro de uma pasta
print(list(Path.cwd().glob('**/*')))

# Validando caminhos
print(Path.home().exists())

# verificando se é arquivo ou pasta
print(Path(__file__).is_file())
print(Path(__file__).parent.is_file())
print(Path(__file__).parent.is_dir())
