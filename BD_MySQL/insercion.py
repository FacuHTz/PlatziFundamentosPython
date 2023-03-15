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
        nombre1 = input("ingrese un nombre de usuario: ")
        sentencia = f"INSERT INTO tipo_usuario (nombre) VALUES ('{nombre1}')"
        #cursor.execute("INSERT INTO tipo_usuario (nombre) VALUES ('Vigilante')")
        cursor.execute(sentencia)
        connection.commit()#confirma la accion que estamos ejecutando
        print("Writnig successful") 

except Error as ex:
    print("Error connecting to database", ex)

finally:
    if connection.is_connected():
        connection.close()
        print("Connection closed")