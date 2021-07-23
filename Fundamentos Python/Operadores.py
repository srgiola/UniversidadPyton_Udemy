# Operadores Aritmeticos

a = 3
b = 2

suma = a + b
print("suma:", suma)

resta = a - b
print("resta:", resta)

multiplicacion = a * b
print("multiplicación:", multiplicacion)

division = a / b
print("divición:", division)

mod = a % b
print("mod:", mod)

exponente = a ** b
print("exponente:", exponente)


# Operadores Asignación

x = 3
print(x)

x += 2  # x = x + 2
print(x)

x -= 1  # x = x - 1
print(x)

x *= 3  # x = x * 3
print(x)

x /= 2  # x = x / 2
print(x)


# Operadores de Comparación

resultado = (a == b)
print(resultado)

resultado = (a != b)
print(resultado)

resultado = (a > b)
print(resultado)

resultado = (a >= b)
print(resultado)

resultado = (a < b)
print(resultado)

resultado = (a <= b)
print(resultado)

if (a%2 == 0):
    print("Es Par")
else:
    print("Es Impar")
    

# Operadores Logicos

a = int(input("Proporciona un valor: "))
valorMax = 0
valorMin = 5
rango = (a >= valorMin and a <= valorMax)
print(rango)

vacaciones = False
diaDescanso = False
if(vacaciones or diaDescanso):
    print("Puedes salir, disfruta rey :)")
else:
    print("Tienes deberes que hacer")

print(not(vacaciones))


# Tarea

alto = int(input("Ingresa el alto:"))
ancho = int(input("Ingresa el ancho"))
print("Area:", (alto * ancho))
print("Perimetro:", ((alto + ancho) * 2)) 

num1 = int(input("Proporciona el numero 1"))
num2 = int(input("Proporciona el numero 2"))
if(num1 > num2):
    print("El numero mayor es:", num1)
else:
    print("El numero mayor es:", num2)