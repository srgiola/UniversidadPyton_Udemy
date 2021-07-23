import os

class CatalogoPeliculas:
    
    #Atributo estatico
    ruta_Archivo = "Peliculas.txt"
    
    #Metodos estaticos
    ''' Decoradores estaticos
    @classmethod #Indica un metodo estatico que recibe el parametro de la clase "cls"
    @staticmethod #Indica un metodo estatico que no recibe parametros de clase
    '''
    @staticmethod 
    def agregarPelicula(pelicula):
        try:
            archivo = open(CatalogoPeliculas.ruta_Archivo, "a")
            archivo.write(pelicula.getNombre() + "\n")
        except Exception as e:
            print(e)
        finally:
            archivo.close()
        
    @classmethod
    def listarPeliculas(cls):
        try:
            archivo = open(cls.ruta_Archivo, "r")
            print("Catalogo de Peliculas: ")
            print(archivo.read())
        except Exception as e:
            print(e)
        finally:
            archivo.close()
        
    @classmethod
    def eliminarPeliculas(cls):
        try:
            os.remove(cls.ruta_Archivo)
            print("Archivo eliminado")
        except Exception as e:
            print(e)
        