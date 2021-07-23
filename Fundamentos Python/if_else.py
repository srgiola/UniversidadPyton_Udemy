condicion = False
if condicion:
    print("La condicion es verdadera")
elif not(condicion): # condicion == False
    print("La condicion es falsa")
else:
    print("Condicion no reconocida")

#IF_Else resumido
print("Condicion verdadera") if condicion else print("Condicion falsa")

 
numero = int(input("Ingrese un numero entre 1 y 3"))
if numero == 1:
    numeroTexto = "Numero 1"
elif numero == 2:
    numeroTexto = "Numero 2"
elif numero == 3:
    numeroTexto = "Numero 3"
else:
    numeroTexto = "Valor fuera de rango"

print("Numero proporcionado:", numeroTexto)


# Tarea 
calificacion = int(input("Ingrese valor entre 0 y 10"))
if calificacion == 9 or calificacion == 10:
    print("A")
elif calificacion == 8:
    print("B")
elif calificacion == 7:
    print("C")
elif calificacion == 6:
    print("D")
elif calificacion >= 0 and calificacion < 6:
    print("F")
else:
    print("Valor desconocido")