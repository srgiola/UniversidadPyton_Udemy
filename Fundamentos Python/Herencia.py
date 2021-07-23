class Persona:
    def __init(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    #Metodo heredado de Object que regresa una cadena, enves de una dirección de
    # memoria cuando se realiza print(Persona)
    def __str__(self):
        return "Nombre: " + self.nombre + " , edad: " + str(self.edad)

#La función "super()" indica que se quiere acceder a los metodos y atributos de
# la clase padre
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad) #Inicializa los parametros de la clase padre
        self.sueldo = sueldo
    
    def __str__(self):
        return super().__str__() + ", sueldo: " + str(self.sueldo)

class Vehiculo:
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas
    
    def __str__(self):
        return "El color del vehiculo es: " + self.color + ", tiene: " + str(self.ruedas) + " ruedas"

class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad
    def __str__(self):
        return super().__str__() + ", llega a una velocidad de: " + str(self.velocidad)

class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo
    
    def __str__(self):
        super().__str__() + ", y es bicicleta tipo: " + self.tipo
         
p1 = Persona("Juan", 28)

e1 = Empleado("Sergio", 22, 6500)
print(e1)