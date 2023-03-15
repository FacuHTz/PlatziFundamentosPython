import mysql.connector
from mysql.connector import Error


class DAO():
    def __init__(self):
        try:
            self.connection= mysql.connector.connect(
                host="localhost",
                port=3306,
                user="root",
                password="tooR",
                db="universidad"
            )
        except Error as ex:
            print(f"error al establecer la conexion: {ex}")

    def listarCursos(self):
        if self.connection.is_connected():
            try:
                cursor=self.connection.cursor()
                cursor.execute("SELECT * FROM cursos ORDER BY nombre ASC")
                resultados = cursor.fetchall()
                return resultados
            except Error as ex:
                print(f"error al ejecutar: {ex}")
    
    def registrarCursos(self, curso):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute(f"INSERT INTO cursos (idCursos, nombre, creditos) VALUES ('{curso[0]}', '{curso[1]}', '{curso[2]}')")
                self.connection.commit()
                print("Curso registrado\n")
            except Error as ex:
                print(f"error al ejecutar: {ex}") 

    def actualizarCurso(self, curso):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute(f"UPDATE cursos SET nombre = '{curso[1]}', creditos = '{curso[2]}' WHERE idCursos = '{curso[0]}'")
                self.connection.commit()
                print("Curso actualizado con total éxito\n")
            except Error as ex:
                print(f"error al ejecutar: {ex}")

    
    
    def eliminarCurso(self, idCursoEliminar):
        if self.connection.is_connected():
            try:
                cursor = self.connection.cursor()
                cursor.execute(f"DELETE FROM cursos WHERE idCursos = '{idCursoEliminar}'")
                self.connection.commit()
                print("Curso eliminado\n")
            except Error as ex:
                print(f"error al ejecutar la conexion: {ex}")

            