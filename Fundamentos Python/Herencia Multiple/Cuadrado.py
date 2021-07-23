from Figura_Geometrica import FiguraGeometrica
from Color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, lado, color):
        #Se ha agregado self ya que se ha antepuesto el Objecto a inicializar
        # y no se uso super el cual ya lo agrega implicitamente
        FiguraGeometrica.__init__(self, lado, lado)
        Color.__init__(self, color)
    
    def area(self):
        return self.alto * self.ancho