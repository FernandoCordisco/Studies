from pathlib import Path
import os

def return_folder_size(directory, folder_analysis, depth):

    directory = (directory / folder_analysis)
    folders = (os.listdir(directory))

    for folder in folders:
            
            size_folder = int()  
            path = directory / folder

            for file in path.glob('**/*'):
                size_file = os.path.getsize(file)
                size_folder = size_file + size_folder 

            size_folder_mb = (size_folder / 1000) / 1000
            print(f'{folder} - {size_folder_mb:.2f}mb')

return_folder_size(Path.home(), 'Documentos', 1)