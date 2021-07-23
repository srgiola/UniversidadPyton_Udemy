class Computadora:
    contadorComputadoras = 0
    
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contadorComputadoras += 1
        self.__idComputadora = Computadora.contadorComputadoras
        self.__nombre = nombre
        self.__monitor = monitor
        self.__teclado = teclado
        self.__raton = raton
        
    def __str__(self):
        return (
            f"Computadora No. {self.__idComputadora}"
            f"\n \t \t Nombre: {self.__nombre}"
            f"\n \t \t Monitor: {self.__monitor.__str__()}"
            f"\n \t \t Teclado: {self.__teclado.__str__()}"
            f"\n \t \t Raton: {self.__raton.__str__()}"
        )
    
class Monitor:
    contadorMonitores = 0
    
    def __init__(self, marca, tamano):
        Monitor.contadorMonitores += 1
        self.__idMonitor = Monitor.contadorMonitores
        self.__marca = marca
        self.__tamano = tamano
        
    def __str__(self):
        return "\n \t \t \t ID: " + str(self.__idMonitor) + "\n \t \t \t Marca: " + self.__marca + "\n \t \t \t Tamaño: " + self.__tamano
    
class DispositivosEntrada:
    def __init__(self, tipo, marca):
        self._tipoEntrada = tipo
        self._marca = marca
    
    def __str__(self):
        return "\n \t \t \t Tipo: " + self._tipoEntrada + "\n \t \t \t Marca: " + self._marca
    
class Raton(DispositivosEntrada):
    contadorRatones = 0
    
    def __init__(self, tipo, marca):
        Raton.contadorRatones += 1
        self.__idRaton = Raton.contadorRatones
        super().__init__(tipo, marca)
    
    def __str__(self):
        return super().__str__() + "\n \t \t \t ID: " + str(self.__idRaton)

class Teclado(DispositivosEntrada):
    contadorTeclado = 0
    
    def __init__(self, tipo, marca):
        Teclado.contadorTeclado += 1
        self.__idTeclado = Teclado.contadorTeclado
        super().__init__(tipo, marca)
    
    def __str__(self):
        return super().__str__() + "\n \t \t \t ID: " + str(self.__idTeclado)

class Orden:
    contadorOrdenes = 0
    
    def __init__(self, Computadoras):
        Orden.contadorOrdenes += 1
        self.__idOrden = Orden.contadorOrdenes
        self.__Computadoras = Computadoras
    
    def agregarComputadora(self, Computadora):
        self.__Computadoras.append(Computadora)
    
    def getIdOrden(self):
        return self.__idOrden
    
    def __str__(self):
        orden = "Orden No. " + str(self.__idOrden) + "\n"
        for computadora in self.__Computadoras:
            orden += "\t" + computadora.__str__() + " \n"
        return orden