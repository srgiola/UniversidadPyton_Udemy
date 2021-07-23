from logger_base import logger

import os

class Persona:
    def __init__(self, idPersona, nombre, apellido, email):
        self.__idPersona = idPersona
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
    
    def __str__(self):
        return (
            f"ID: {self.__idPersona}, "
            f"Nombre: {self.__nombre}, "
            f"Apellido: {self.__apellido}"
            f"Email: {self.__email}"
        )
        
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getEmail(self):
        return self.__email
    
    def getID(self):
        return self.__idPersona
        
if __name__ == "__main__":
    os.system("cls")
    persona1 = Persona(1, "Juan", "Pacheco", "jpa@mail.com")
    logger.debug(persona1)