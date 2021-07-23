#Encapsulamiento es ocultar el acceso directo a los atributos de una clase

#En Python todas las clases son de tipo public por defecto. 
class Persona:
    def __init__(self, nombre):
        #Al agregar los dos guines bajos se indica que el atributo es privado
        self.__nombre = nombre
        self.__edad = 19
    
    def get_nombre(self):
        return self.__nombre
    
    def get_edad(self):
        return self.__edad
    
    def set_nombre(self, nombre):
        self.__nombre = nombre
        
p1 = Persona("Juan")
#print(p1.__nombre) Esto da error ya que el atributo es privado
#p1.__nombre = "Karla" Esta tambien da error por la misma razón
p1.set_nombre("Karla")
print(p1.get_nombre())




