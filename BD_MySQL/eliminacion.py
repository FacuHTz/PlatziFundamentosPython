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
        cursor.execute("DELETE FROM tipo_usuario WHERE id='4' AND validity = '0'")
        connection.commit()#confirma la accion que estamos ejecutando
        print("Deleting successful") 

except Error as ex:
    print("Error connecting to database", ex)

finally:
    if connection.is_connected():
        connection.close()
        print("Connection closed")