import os
from zipfile import ZipFile
import shutil

docs = os.walk("C:/Users/Acer/Documents/Material importante/Proyecto NLP/Etiquetado/Curacion BIO", 
               topdown=False)

for directorio_actual, subdirectorios, archivos in docs:
    # directorio_actual es una cadena que representa la ruta del directorio actual
    print("Directorio actual:", directorio_actual)

    # subdirectorios es una lista de cadenas que contiene los nombres de los subdirectorios en el directorio actual
    print("\n Subdirectorios:", subdirectorios)

    # archivos es una lista de cadenas que contiene los nombres de los archivos en el directorio actual
    print("\n Archivos:", archivos)


arc_zip = []
name = []
for root, dirs, files in docs:
   for name in files:
       #print(name)
       if '.zip' in name:
           arc_zip.append(os.path.join(name))

#%% MELO
for i in range(len(dirs)):
    contenido = os.chdir("C:/Users/Acer/Desktop/Curacion BIO/curation/{}".format(dirs[i]))
    with ZipFile(arc_zip[i], 'r') as zip:
        zip.extractall()
        
    # with os.scandir(contenido) as ficheros:
    #     for fichero in ficheros:
    #         print(fichero.name)
    
    now_name = os.path.join("C:/Users/Acer/Desktop/Curacion BIO/curation/{}".format(dirs[i]), 
                            "CURATION_USER.xmi")
    new_name = os.path.join("C:/Users/Acer/Desktop/Curacion BIO/curation/{}".format(dirs[i]), 
                            "{}.xmi".format(dirs[i]))
    
    shutil.move(now_name, new_name)
    
    
    source = '{}.xmi'.format(dirs[i])
    destination = "C:/Users/Acer/Desktop/Curacion BIO"

    shutil.move(source,destination)
    
typesystem = 'TypeSystem.xml'
shutil.move(typesystem,destination)