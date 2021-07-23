from Clases import *

producto1 = Producto("Camsisa", 100.00)
producto2 = Producto("Pantalon", 110.00)
producto3 = Producto("Calcetines", 50.00)

productos = [producto1, producto2]
orden1 = Orden(productos)

orden2 = Orden(productos)
orden2.agregarProducto(producto3)

print(str(orden1.calcularTotal()))

#Ambas ordenes tienen los mismos valores ya que ambos
# estan apuntando a la misma lista internamente, por lo que si 
# se agrega un valor nuevo a la lista este tambien se agregara 
# en la lista que esta dentro del objeto instanciado
# que mamada xd
print(orden1)
print(orden2)