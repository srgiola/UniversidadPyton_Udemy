#Abre un archivo
# open() tiene dos parametros, el primero el archivo y el segundo lo que se desea hacer
# r - Read the default value. Da error si no existe el archivo
# a - Agrega info al archivo. Si no existe lo crea
# w - Escribir en un archivo. Si no existe lo crea. Sobreescribe el archivo
# x - Crea un archivo. Retorna error si el archivo ya existe
try:
    archivo = open("File_Manejo_Archivos.txt", "w")
    archivo.write("Agregando información al archivo \n")
    archivo.write("Agregando linea 2")
    
    archivo = open("File_Manejo_Archivos.txt", "r")
    ''' Formas de leer un archivo
    print(archivo.read())           # Leer archivo completo
    print(archivo.read(5))          # Numero de caracteres a leer
    print(archivo.readline())       # Leer una linea
    print(archivo.readlines())      # Lee todas las linea, agrega todo a una lista
    print(archivo.readlines()[1])   # Lee solo la linea con indice 1
    
    for linea in archivo:
        print(linea)
    '''
    # Copiando un archivo a otro
    archivo2 = open("File_Copia.txt", "w")
    archivo2.write(archivo.read())
     
except Exception as e:
    print(e)
finally:
    archivo.close() # No es obligatorio
    archivo2.close()