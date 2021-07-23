from Cuadrado import Cuadrado

c1 = Cuadrado(2, "Rojo")
print(c1.area())
print(c1.color)

# mro - Method Resulution Object
# indica cual es el orden que se tiene para cada clase padre
print(Cuadrado.mro()) 