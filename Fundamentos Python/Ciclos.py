#While

condicion = False
while condicion:
    print("Ejecutando ciclo while")
else:
    print("Fin ciclo while")
    
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("Fin Ciclo While")
    

#For

for letra in "Hola": #For each
    print(letra)
else:
    print("Fin ciclo for")

palabra = "Hola"
for i in range(4):
    print(palabra[i])

# Con break se cierra todo el ciclo, incluso se salta el else del ciclo
for letra in "Holanda":
    if letra == "a":
        print(letra)
        break 
else
    print("Fin de Ciclo")
    
# Con continue se le dice al interprete que continue con la siguiente iteración
# y que no ejecute el codigo que falta en la iteración
for i in range(6):
    if i%2 != 0:
        continue
    print(i)