class Producto:
    contador_productos = 0
    
    def __init__(self, nombre, precio):
        Producto.contador_productos += 1
        self.__nombre = nombre
        self.__precio = precio
        self.__idProducto = Producto.contador_productos
        
    def __str__(self):
        return "ID Producto: " + str(self.__idProducto) + ", Nombre: " + self.__nombre + ", Precio: " + str(self.__precio)
    
    def getPrecio(self):
        return self.__precio

class Orden:
    contador_ordenes = 0
    
    def __init__(self, productos):
        Orden.contador_ordenes += 1
        self.__idOrden = Orden.contador_ordenes
        self.__productos = productos
    
    def __str__(self):
        productos_str = ""
        for producto in self.__productos:
            productos_str += producto.__str__() + " \n "
        
        return "Orden: " + str(self.__idOrden) + "\n" + productos_str
    
    def agregarProducto(self, producto):
        self.__productos.append(producto)
        print("Producto agregado exitosamente")
    
    def calcularTotal(self):
        total = 0.0
        for producto in self.__productos:
            total += producto.getPrecio()
        return total