from logger_base import logger
from Conexion import Conexion
from Persona import Persona

import os

#DAO = Data Access Object
class PersonaDAO:
    __select = 'SELECT * FROM "Persona" ORDER BY "Id_Persona"'
    __insert = 'INSERT INTO "Persona"("Nombre", "Apellido", "Email") VALUES(%s, %s, %s)'
    __update = 'UPDATE "Persona" SET "Nombre"=%s, "Apellido"=%s, "Email"=%s WHERE "Id_Persona"=%s'
    __delete = 'DELETE FROM "Persona" WHERE "Id_Persona"= %s'
    
    @classmethod
    def selecionar(cls):
        cursor = Conexion.obtenerCursor()
        logger.debug(cursor.mogrify(cls.__select))
        cursor.execute(cls.__select)
        registros = cursor.fetchall()
        personas = []
        for registro in registros:
            persona = Persona(registro[1], registro[2], registro[0], registro[3])
            personas.append(persona)
        
        Conexion.cerrar()
        return personas
    
    @classmethod
    def insertar(cls, persona):
        try:
            db = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__insert))
            logger.debug(f"Persona a insertar: {persona}")
            valores = (persona.getNombre(), persona.getApellido(), persona.getEmail())
            cursor.execute(cls.__insert, valores)
            db.commit()
            return cursor.rowcount
        except Exception as e:
            db.rollback()
            logger.error(f"Excepción al insertar persona: {e}")
        finally:
            Conexion.cerrar()
            
    @classmethod
    def actualizar(cls, persona):
        try:
            db = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__update))
            logger.debug(f"Persona a actualizar: {persona}")
            valores = (persona.getNombre(), persona.getApellido(), persona.getEmail(), persona.getID())
            cursor.execute(cls.__update, valores)
            db.commit()
            return cursor.rowcount
        except Exception as e:
            db.rollback()
            logger.error(f"Excepción al actualizar persona: {e}")
        finally:
            Conexion.cerrar()
            
    @classmethod
    def eliminar(cls, persona):
        try:
            db = Conexion.obtenerConexion()
            cursor = Conexion.obtenerCursor()
            logger.debug(cursor.mogrify(cls.__delete))
            logger.debug(f"Persona a eliminar: {persona}")
            valores = (persona.getID(),)
            cursor.execute(cls.__delete, valores)
            db.commit()
            return cursor.rowcount
        except Exception as e:
            db.rollback()
            logger.error(f"Excepción al eliminar persona: {e}")
        finally:
            Conexion.cerrar()
    
    
if __name__ == "__main__":
    os.system("cls")
    
    personas = PersonaDAO.selecionar()
    for persona in personas:
        logger.debug(persona)
    
    
    persona = Persona(None, "Pedro", "Najera", "pnagera@gmail.com")
    personas_insertadas = PersonaDAO.insertar(persona)
    logger.debug(f"Personas insertadas: {personas_insertadas}")
    
    
    persona = Persona(10, "Sergio", "Lara", "slara@gmail.com")
    personas_actualizadas = PersonaDAO.actualizar(persona)
    logger.debug(f"Personas actualizadas: {personas_actualizadas}")
    
    persona = Persona(11, "Sergio", "Lara", "slara@gmail.com")
    personas_eliminadas = PersonaDAO().eliminar(persona)
    logger.debug(f"Personas eliminadas: {personas_eliminadas}")
    