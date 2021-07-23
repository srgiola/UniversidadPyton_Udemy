import os
import psycopg2

os.system("cls")

# ----- Conexión a la BD -----

db = psycopg2.connect(user="postgres",
                      password="1909",
                      host="localhost",
                      port="5432",
                      database="test_db")

cursor = db.cursor()

# ----- Select -----

query = 'select * from "Persona" where "Id_Persona" = %s'
# el '%s' es un parametro que se enviara desde python a la BD
Id_Persona = input("Indica la PK a buscar: ")
llave_primaria = (Id_Persona,)

cursor.execute(query, llave_primaria)
# Como sabemos que solo hay un ID=1 podemos usar 'fetchone'
registros = cursor.fetchone()
print(registros)


query2 = 'select * from "Persona" where "Id_Persona" in %s'
entrada = input("Ingrese las PK a buscar: ")
tupla = tuple(entrada.split(","))
print(tupla)
# Si es mas de un parametro a pasar, se usa como parametro
llaves_primarias = (tupla,)
#   una tupla de tuplas

cursor.execute(query2, llaves_primarias)
registros = cursor.fetchall()
print(registros)


# ----- Insert -----

query3 = 'insert into "Persona"("Nombre", "Apellido", "Email") values(%s, %s, %s)'
valores = ("Carlos", "Lara", "clara@mail.com")
cursor.execute(query3, valores)
db.commit()
registros_insertados = cursor.rowcount
print(f"Registros insertados: {registros_insertados}")


query4 = 'insert into "Persona"("Nombre", "Apellido", "Email") values(%s, %s, %s)'
valores = (
    ('Carlos', 'Lara', 'clara@gmail.com'),
    ('Luis', 'Gomez', 'lgomez@gmail.com'),
    ('Marcos', 'Alcantara', 'malcantara@gmail.com')
)
cursor.executemany(query4, valores)
db.commit()
registros_insertados = cursor.rowcount
print(f"Registros insertados: {registros_insertados}")


# ----- Update -----

query5 = 'update "Persona" set "Nombre" = %s, "Apellido" = %s, "Email" = %s where "Id_Persona" = %s'
valores = (("Juan", "Perez", "jperez@gmail.com", 10),)
cursor.execute(query5, valores)
db.commit()
registros_actualizados = cursor.rowcount
print(f"Registros actualizados: {registros_actualizados}")


query6 = 'update "Persona" set "Nombre" = %s, "Apellido" = %s, "Email" = %s where "Id_Persona" = %s'
valores = (
    ("Juan", "Perez", "jperez@gmail.com", 10),
    ("Sergio", "Lara", "slara@gmail.com", 11)
)
cursor.executemany(query6, valores)
db.commit()
registros_actualizados = cursor.rowcount
print(f"Registros actualizados: {registros_actualizados}")


# ----- Delete -----

query7 = 'delete from "Persona" where "Id_Persona" = %s'
entrada = input("Indique la PK del registro a eliminar: ")
valores = (entrada,)
cursor.execute(query7, valores)
db.commit()
registros_eliminados = cursor.rowcount
print(f"Registros eliminados: {registros_eliminados}")


query8 = 'delete from "Persona" where "Id_Persona" = %s'
entrada = input("Indique las PKs de los registros a eliminar: ")
tupla = tuple(entrada.split(","))
valores = (tupla,)
cursor.execute(query8, valores)
db.commit()
registros_eliminados = cursor.rowcount
print(f"Registros eliminados: {registros_eliminados}")

cursor.close()
db.close()
