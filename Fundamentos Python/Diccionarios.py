# Key, Value

diccionario = {
    "IDE": "Integrated Development Environment", "OOP": "Object Oriented Programing",
    "DBMS": "Database Management System"
}
print(diccionario)

# Largo del diccionario
print(len(diccionario))
print(diccionario.__len__())

#Acceder a un elemento
print(diccionario["IDE"])
print(diccionario.get("IDE"))

#Modificar Valor
diccionario["IDE"] = "integrated development environment"

#Iterar
for key in diccionario:
    print(key)
    
for key in diccionario:
    print(diccionario[key])

for value in diccionario.values():
    print(value)

#Comprobar existencia de un elemento
print("IDE" in diccionario)

#Agregar elementos
diccionario["PK"] = "Primary Key" 

#Remover elementos
diccionario.pop("DBMS")

# Limpiar el diccionario
diccionario.clear()

