from Clases import *

teclado1 = Teclado("USB", "HP")
teclado2 = Teclado("USB", "Microsoft")
teclado3 = Teclado("USB", "Logitech")

monitor1 = Monitor("HP", "27 pulgadas")
monitor2 = Monitor("Dell", "22 pulgadas")
monitor3 = Monitor("Acer", "15 pulgadas")

raton1 = Raton("USB", "XTech")
raton2 = Raton("USB", "Microsoft")
raton3 = Raton("USB", "Logitech")

computadora1 = Computadora("Idepad", monitor1, teclado1, raton1)
computadora2 = Computadora("Galeon", monitor2, teclado2, raton2)
computadora3 = Computadora("Dell 510", monitor3, teclado3, raton3)

Computadoras = [computadora1, computadora2]
orden1 = Orden(Computadoras)
print(orden1)

orden2 = Orden(Computadoras)
orden2.agregarComputadora(computadora3)
print(orden2)