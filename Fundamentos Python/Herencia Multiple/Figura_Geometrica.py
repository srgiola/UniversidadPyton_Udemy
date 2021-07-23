#Cuando se agrega una función abstracta automaticamente se 
# se vuelve abstracta la clase

#ABC = Abstract Base Class
from abc import ABC, abstractmethod

class FiguraGeometrica(ABC):
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto
    
    @abstractmethod
    def area(self):
        pass