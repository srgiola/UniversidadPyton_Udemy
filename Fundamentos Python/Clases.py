class Persona:
    #Contructor
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Aritmetica:
    #Constructor
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
    
    def suma(self):
        return self.num1 + self.num2

class Retangulo:
    #Constructor
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def calcularArea(self):
        return self.base * self.altura

class Caja:
    #Contructor
    def __init__(self, largo, ancho, alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
    
    def Volumen(self):
        return self.largo * self.ancho * self.alto

#El parametro self se puede cambiar por cualquier otro palabra siempre y 
# cuando se utilice de la misma manera, asi mismo se puede colocar otros
# nombres a los parametros y lo que quedaran como nombres de los atributos
# son los que esten con self

class Carro:
    #Constructor
    def __init__(this, n, e, *v, **d): #El "*" significa que el parametro es una tupla y es opcional
        this.marca = n                 # el "**" significa que el parametro es un diccionario y es opcional
        this.modelo = e
        this.valores = v
        this.diccionario = d
    
    def desplegar(this):
        print("Marca:", this.marca)
        print("Modelo:", this.modelo)
        print("Valores (Tupla):", this.valores)
        print("Dicionario:", this.diccionario)

carro = Carro("Toyota", "Yaris", 2,4,5)
print(carro.desplegar())

carro2 = Carro("Volvo", "S40", 4,9,5, m="Manzana", p="Pera", j="Jicama")
print(carro2.desplegar())

#Instanciar una clase
persona = Persona("Sergio", 22)
print(persona.nombre, persona.edad)

aritmetica = Aritmetica(2, 4)
print("Resultado suma:", aritmetica.suma())

base = int(input("Ingrese base del Retangulo: "))
altura = int(input("Ingrese altura del retangulo: "))
retangulo = Retangulo(base, altura)
print(retangulo.calcularArea())

