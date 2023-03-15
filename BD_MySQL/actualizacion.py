import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",
        password="tooR",
        db="condominio"
    )
    if connection.is_connected():
        print("Connection established successfully")
        cursor = connection.cursor()
        cursor.execute("UPDATE tipo_usuario SET nombre = 'Huesped', validity = 0 WHERE nombre = 'Visitante'")
        connection.commit()#confirma la accion que estamos ejecutando
        print("Updating successful") 

except Error as ex:
    print("Error connecting to database", ex)

finally:
    if connection.is_connected():
        connection.close()
        print("Connection closed")