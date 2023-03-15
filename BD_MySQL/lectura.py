import mysql.connector
from mysql.connector import Error
"""
Un cursor es una estructura de control que se usa para recorrer y procesar los registros del resultado de una consulta a una base de datos³. En Python, se crea un cursor usando el método .cursor() de un objeto de conexión⁴. El cursor permite ejecutar sentencias SQL y obtener los datos devueltos⁵.

Origen: Conversación con Bing, 3/5/2023(1) Cursor (base de datos) - Wikipedia, la enciclopedia libre. https://es.wikipedia.org/wiki/Cursor_(base_de_datos) Con acceso 3/5/2023.
(2) Manejo de bases de datos en Python - Code Envato Tuts+. https://code.tutsplus.com/es/tutorials/manejo-de-bases-de-datos-en-python--cms-25645 Con acceso 3/5/2023.
(3) Acceso a base de datos SQLite usando Python y Pandas. https://datacarpentry.org/python-ecology-lesson-es/09-working-with-sql/index.html Con acceso 3/5/2023.
(4) ¿Qué es un cursor? (Referencia de base de datos de escritorio de Access .... https://bing.com/search?q=que+es+un+cursor+en+el+proceso+de+conexion+de+un+archivo+python+a+una+base+de+datos Con acceso 3/5/2023.
(5) ¿Qué es un cursor? (Referencia de base de datos de escritorio de Access .... https://learn.microsoft.com/es-es/office/client-developer/access/desktop-database-reference/what-is-a-cursor Con acceso 3/5/2023.
"""
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
        cursor = conexion.cursor()
        cursor.execute("SELECT database()")#al escribir database automaticamente nos devuelve el nombre de la base de datos a la cual nos conectamos
        registro=cursor.fetchone() #fetch se refiere a la acción de obtener o recuperar los datos que resultan de una consulta SQL
        #El método cursor.fetchall() devuelve una lista de tuplas que contienen los datos de cada fila de la tabla clientes. Puedes iterar sobre esta lista para acceder a los datos. También puedes usar otros métodos como cursor.fetchone() o cursor.fetchmany() para obtener solo una fila o un número determinado de filas.
        print(registro)
        cursor.execute("SELECT * FROM tipo_usuario")
        tipo_usuario=cursor.fetchall()
        for fila in tipo_usuario:#como tenemos varias entradas de esa tabla, podemos listarlos usando un ciclo, para eso recorremos las columnas
            print(fila[0], fila[1], fila[2])
        print("Total de registros", cursor.rowcount)
            
            
except Error as ex:
    print("error a la conexion", ex)

finally:
    if conexion.is_connected():
        conexion.close()
        print("connection closed")