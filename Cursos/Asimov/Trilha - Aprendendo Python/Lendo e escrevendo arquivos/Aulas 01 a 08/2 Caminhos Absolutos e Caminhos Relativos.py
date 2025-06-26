from pathlib import Path

pasta_existe = Path('Aulas 01 a 08').exists()
print(pasta_existe)

print(Path.cwd())