class Empleado:
    def __init__(self, nombre, sueldo):
        self.nombre = nombre
        self.sueldo = sueldo
    
    def __str__(self):
        return "Nombre: " + self.nombre + " Sueldo: " + str(self.sueldo)
    
class Gerente(Empleado):
    def __init__(self, nombre, sueldo, departamento):
        super().__init__(nombre, sueldo)
        self.departamento = departamento
    
    def __str__(self):
        return super().__str__() + " Departamento: " + self.departamento
    
def imprimirDetalles(tipo_padre):
    print(tipo_padre)
    print(type(tipo_padre), end= "\n \n")
    
    if isinstance(tipo_padre, Gerente):
        print(tipo_padre.departamento)

empleado = Empleado("Juan", 1000.00)
imprimirDetalles(empleado)

empleado2 = Gerente("Karla", 2000.50, "Sistemas")
imprimirDetalles(empleado2)