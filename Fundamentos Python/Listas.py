nombres = ["Juan", "Sergio", "Maria", "Lis"]
print(nombres)

print(len(nombres)) # len() retorna el numero de elementos contenidos

print(nombres[0]) # Se solicita indice cero

print(nombres[-1]) # Se solicita el ultimo elemento

print(nombres[1:3]) # Imprime rango de 1 al 2

print(nombres[:3]) # Imprime del 0 al 2

print(nombres[1:]) # Imprime los elementos hasta el final desde el indice proporcionado

nombres[3] = "Ivone"
print(nombres)

# Iterar la lista
for nombre in nombres:
    print(nombre)

# Revisar si existe un elemento en la lista
if "Karla" in nombres:
    print("Karla si existe en la lista")
else:
    print("El elemento buscado no existe en la lista")

# Agregar un elemento 
nombres.append("Lorenzo")

# Agregar nuevo elemento en el indice indicado
nombres.insert(1, "Octavio")

# Remover un elemento
nombres.remove("Octavio")

# remover el ultimo elemento
nombres.pop()

# remover el elemento en el indice indicado
del nombres[1]

# Limpiar todos los elementos de la lista
nombres.clear()

# Eliminar de memoria la lista
del nombres


#Tarea
numeros = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for numero in numeros:
    if numero % 3 == 0:
        print(numero)