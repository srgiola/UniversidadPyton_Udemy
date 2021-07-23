class Persona:
    def __init__(self, nombre, apellido, apodo):
        self.nombre = nombre        #Atributo public
        self._apellido = apellido   #Atributo protected "_"
        self.__apodo = apodo        #Atributo privado "__"
    
    def metodoPublico(self):
        self.__metodoPrivado()
    
    def __metodoPrivado(self):
        print(self.nombre)
        print(self._apellido)
        print(self.__apodo)

p1 = Persona("Sergio", "Lara", "Chejo")

print(p1.nombre)
print(p1._apellido)