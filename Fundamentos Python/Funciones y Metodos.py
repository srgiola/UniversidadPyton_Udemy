def mi_funcion():
    print("Ejecutando mi función")

def funcion_arg(nombre):
    print("El nombre recibido es:", nombre)
    
def suma(a, b):
    return a + b;

def suma_default(a = 0, b = 0):
    return a + b;

mi_funcion()

funcion_arg("Sergio")

print(suma(5, 3))
