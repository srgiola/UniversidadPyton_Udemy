#Una variable de clase, son las variables que se encuentran
# asociadas a la clase como objeto y no a los derivados que serian las
# instancias. Ya que un valor definido en la clase y luego se modifique,
# este cambio no va a afectar a todos los objetos instanciados. 

class MiClase:
    variable_clase = "Variable de clase"
    
    def __init__(self, variable_instancia):
        self.variableInstancia = variable_instancia
    
print(MiClase.variable_clase)
objeto1 = MiClase("variable_instancia")
MiClase.variableInstancia = "Modificando variable instancia"
print(MiClase.variableInstancia)
print(objeto1.variableInstancia)

print(objeto1.variable_clase)
objeto1.variable_clase = "Hola"
print(MiClase.variable_clase)
print(objeto1.variable_clase)