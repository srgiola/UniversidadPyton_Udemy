# clic derecho sobre el nombre del archivo (Pestaña superior) en
# "Open Preview to the side" para ver como funcionara el programa
# en tiempo real y con los valores de las variable.

x = 3
y = 5
z = x + y
print(z);
w = z #Aca "w" y "z" ocupan la misma dirección de memoria

#id(x) 
#Eso sirve para visualisar la dirección de memoria,
#pero solo en el IDE de Python

a = 1 # int
b = 1.2 # float
c = "Hola" # string
d = False # bool

print(c + str(x + y)) #Para concatenear strings con numeros se deben convertir primero
print(c, x + y) #Al usar coma si se pueden concatenar pero siempre agrega un espacio

num1 = 1
num2 = 2
resultado = num1 < num2 #Esto es un IF implicito
print(resultado)

if(num1 < num2):
    print("El valor num1 es menor que num2")
else:
    print("El valor num1 no es menor que num2")