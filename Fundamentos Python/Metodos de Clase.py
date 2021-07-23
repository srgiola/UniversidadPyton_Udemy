class MiClase:
    
    variable_clase = "Variable Clase"
    
    def __init__(self):
        self.variable_instancia = "Variable Instancia"
    
    @staticmethod #Metodo estatico que no recibe parametros de clase
    def metodo_estatico():
        print("Metodo estatico")
        print(MiClase.variable_clase)
        
    @classmethod #Metodo estatico que recibe el parametro de clase cls"
    def metodo_clase(cls):
        print("Metodo de clase: " + str(cls))
        print(cls.variable_clase)
    
    def metodo_instancia(self):
        self.metodo_clase()
        self.metodo_estatico()

MiClase.metodo_estatico()
MiClase.metodo_clase()

Objeto1 = MiClase()
Objeto1.metodo_instancia()
