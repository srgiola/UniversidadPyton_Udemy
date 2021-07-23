# Set es una colección sin orden y sin indices, tampoco permite elementos repetidos
#  y los elementos no se pueden modificar, pero si agregar nuevos o eliminar
planetas = {"Marte", "Jupiter", "Venus"}
print(planetas)

print(len(planetas))

print("Marte" in planetas) #Revisar si existe un elemento, devuelve boleano

planetas.add("Tierra") #Agregar un elemento

planetas.remove("Tierra") #Remover un elemento

planetas.discard("Tierra") # Remueve un elemento pero no muestra excepción

planetas.clear() #Limpia el set

del (planetas) #Elimina el set