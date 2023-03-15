import mysql.connector
from mysql.connector import Error

#ahora nos vamos a conectar a una base de datos previamente configurada a traves de python, en este caso es una MySQL y esta es la sentencia para hacerlo, ya habiamos probado el try/except que nos ayuda a tener una devolucion mas clara en caso de error
try:
    conexion = mysql.connector.connect( #para conectarnos necesitamos indicarle algunos parametros de conexion
        host="localhost", #para saber a que ip nos tenemos que conectar, en este caso localhost
        port=3306, #el puerto de esa ip al que nos conectamos
        user="root", #el usuario a traves del cual entramos a la base de datos
        password="tooR", #la contraseña de ese usuario
        db="condominio" #la base de datos a la cual vamos a conectarnos dentro de ese puerto
    )
    if conexion.is_connected():
        print("Conexion established")
        infoServer=conexion.get_server_info()
        print("Info del server: " + infoServer)
except Error as ex:
    print("error a la conexion", ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print("connection closed")

""" propuesta de CODEGPT
Existen varios métodos para conectar una base de datos MySQL a Python. Uno de los más populares es el uso de la biblioteca PyMySQL, que es una implementación nativa en Python para trabajar con bases de datos MySQL. 

Para comenzar, debes instalar la biblioteca PyMySQL usando pip o cualquier otro gestor de paquetes para Python: 

Para una instalación con pip: 
pip install pymysql 

A continuación, necesitarás importar la biblioteca en tu script (puedes llamarlo db_connection.py): 
import pymysql 

 Ahora debes establecer los parámetros para realizar una conexión a la base de datos MySQL. Estas son las variables que tendrás que definir: dbhost, dbport, dbuser, dbpass y dbname. Para el puerto, si no se especifica ninguno, se asume 3306 por defecto para MySQL. A continuación se muestra un ejemplo: 
dbhost = 'localhost'   # Dirección del host donde se almacena tu base de datos MySQL 
dbport = 3306          # Puerto utilizado por el servidor MySQL (por defecto es 3306) 
dbuser = 'root'        # Nombre del usuario de la base de datos MySQL 
dbpass = 'password'    # Contraseña del usuario de la base de datos MySQL 
dbname = 'my_database' # Nombre de la base de datos que quieres conectar (ej: my_database)  

 Una vez que hayas definido todas las variables anteriores, puedes proceder a conectarte a la base de datos utilizando las siguientes líneas de código: 

 connection = pymysql.connect(host=dbhost, port=dbport, user=dbuser, passwd=dbpass, db=dbname)

 Ahora ya estás conectado a tu base de datos y puedes realizar tareas como consultas SQL. Para realizar consultas SQL puedes usar el siguiente código:  

 try:     

     with connection.cursor() as cursor:         

         sql = "SELECT * FROM users"         

         cursor.execute(sql)         

         result = cursor.fetchall()         

         print(result)     

     finally:         

         connection.close()  

 Y listo! Ya tienes un ejemplo básico para comenzar a trabajar con bases de datos MySQL desde Python utilizando PyMySQL.
 """