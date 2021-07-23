#Para importar una clase es diferente que un modulo con funciones o codigo simple
# se debe realizar utilizando la sintaxis de:
# "from <Folder>.<File> import <Class>" 
# Si esta en la misma carpeta solo indicar el <File>
from Clases.Persona import Persona as PersonaClase

p1 = PersonaClase("Sergio", 22)
print(p1)