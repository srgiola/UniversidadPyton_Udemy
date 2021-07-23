from logger_base import logger

import psycopg2
import sys
import os

class Conexion:
    
    __database = "test_db"
    __userName = "postgres"
    __password = "1909"
    __dbPort = "5432"
    __host = "localhost"
    __cursor = None
    __db = None
        
    @classmethod
    def obtenerConexion(cls):
        if cls.__db is None:
            try:
                cls.__db = psycopg2.connect(user = cls.__userName,
                                        password = cls.__password,
                                        host = cls.__host,
                                        port = cls.__dbPort,
                                        database = cls.__database)
                logger.debug(f"Conexión exitosa: {cls.__db}")
                return cls.__db
            except Exception as e:
                logger.error(f"Error conectar a la BD: {e}")
                sys.exit()
        else:
            return cls.__db
    
    @classmethod
    def obtenerCursor(cls):
        if cls.__cursor is None:
            try:
                cls.__cursor = cls.obtenerConexion().cursor()
                logger.debug(f"Se abrio el cursor con exito: {cls.__cursor}")
                return cls.__cursor
            except Exception as e:
                logger.error(f"Error al obtener cursor: {e}")
                sys.exit()
        else:
            return cls.__cursor
    
    @classmethod
    def cerrar(cls):
        if cls.__cursor is not None:
            try:
                cls.__cursor.close()
                logger.debug("Se ha cerrado el cursor")
            except Exception as e:
                logger.error(f"Error al cerrar cursor {e}")
        if cls.__db is not None:
            try:
                cls.__db.close()
                logger.debug("Se ha cerrado la conexión")
            except Exception as e:
                logger.error(f"Error al cerrar conexión: {e}")
                




if __name__ == '__main__':
    os.system("cls")
    logger.info(Conexion.obtenerConexion())
    logger.info(Conexion.obtenerCursor())
    Conexion.cerrar()
    
    
