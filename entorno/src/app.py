from db import get_connection

try:
    connection = get_connection()
    with connection.cursor() as cursor:
        query = 'SELECT idCursos, nombre FROM cursos WHERE idCursos = 12457'
        cursor.execute(query)
        row = cursor.fetchone()
        print(row)
    connection.close()
except Exception as ex:
    print(ex)