# La tupla luego de ser inicializada no se puede modificar
frutas = ("Naranja", "Platano", "Guayaba")
print(frutas)

print(len(frutas))

print(frutas[0]) # Acceder a un elemento

print(frutas[-1]) # Navegación inversa

#Tambien funcionan los rangos igual que en las listas
print(frutas[0:2]) 

# Una Lista se puede inicializar con una tubpla
frutasLista = list(frutas)
frutasLista[1] = "Platanito"

# Una tupla se puede modificar, metiendo una lista que sustituye su valor
frutas = tuple(frutasLista)

# Iterar sobre la tupla, esto se realiza de igual manera que con las listas
for fruta in frutas:
    print(fruta, end=" ") #El end=" " indica como queremos que finalize el imprimir fruta


#Tarea
tupla = (13, 1, 8, 3, 2, 5, 8)
lista = []
for t in tupla:
    if t < 5:
        lista.append(t)
print(lista)
