#Creando mi propia clase de Exception
class NumerosIdenticosException(Exception): #Siempre se hereda de Exception
    def __init__(self, mensaje):
        self.message = mensaje