from pathlib import Path
import xml.dom.minidom as x

pasta_atual = Path(__file__).parent

#Lendo arquivo XML

domtree = x.parse(str(pasta_atual / 'xmls' / 'livros.xml'))
group = domtree.documentElement
livros = group.getElementsByTagName('livro')

#Interando por elementos e retornando valores

for livro in livros:
    titulo = livro.getElementsByTagName('titulo')[0].childNodes[0].nodeValue
    genero = livro.getElementsByTagName('genero')[0].childNodes[0].nodeValue
    autor = livro.getElementsByTagName('autor')[0].childNodes[0].nodeValue
    print('titulo:', titulo, '/ Autor:', autor, '/ Genêro:', genero )

#Salvando um arquivo XML:

livros[0].getElementsByTagName('titulo')[0].childNodes[0].nodeValue = 'Vilela, Fernando'

with open(pasta_atual / 'xmls' / 'livros_copia.xml', 'w') as f:
    domtree.writexml(f)



