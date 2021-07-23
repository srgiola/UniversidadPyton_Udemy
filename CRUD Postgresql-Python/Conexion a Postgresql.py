import psycopg2

conexion = psycopg2.connect(user="postgres",
                             password="1909",
                             host="localhost",
                             port="5432",
                             database="test_db")

# Permite enviar sentencias sql a la Base de datos
cursor = conexion.cursor()
query = 'select * from "Persona"'
cursor.execute(query)

registros = cursor.fetchall()
print(registros)

cursor.close()
conexion