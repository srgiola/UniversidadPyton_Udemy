import os
import psycopg2

os.system("cls")

db = psycopg2.connect(user="postgres",
                      password="1909",
                      host="localhost",
                      port="5432",
                      database="test_db")

# Si durante la transacción una operaciones falla, automaticamente falla toda la transacción
try:
    # db.autocommit = True
    cursor = db.cursor()

    query = 'INSERT INTO "Persona"("Nombre", "Apellido", "Email") VALUES(%s, %s, %s)'
    valores = ("Evelyn", "Vasquez", "evasquez@gmail.com")
    cursor.execute(query, valores)
   
    query2 = 'UPDATE "Persona" SET "Nombre" = %s, "Apellido" = %s, "Email" = %s WHERE "Id_Persona" = %s'
    valores("Juan", "Perez", "jperez@gmail.com", 1)
    cursor.execute(query2, valores)
    
    db.commit()

except Exception as e:
    print(f"Ocurrio un error en la transacción: {e}")
    #Rollback da marcha atras a todas las operaciones pendientes
    db.rollback()
finally:
    cursor.close()
    db.closer()
