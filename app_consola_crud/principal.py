from BD.conexion import DAO
import funciones
from mysql.connector import Error


def menu_principal():
    continuar=True
    while(continuar):
        seleccionCorrecta = False
        while (not seleccionCorrecta):
            print("=============== Menu Principal ===================")
            print("1.Listar cursos")
            print("2.Registrar curso")
            print("3.Acualizar curso")
            print("4.Borrar curso")
            print("5.Salir del programa")
            print("==================================================")
            seleccion = int(input("Seleccione una opcion "))
            
            if seleccion < 1 or seleccion > 5:
                print("Opcion incorrecta, seleccione otra opcion")
            elif seleccion == 5:
                continuar = False
                print("Gracias por usar el progrma")
                break
            else:
                seleccionCorrecta = True    
                ejecutarSeleccion(seleccion)


def ejecutarSeleccion(seleccion):
    dao = DAO()

    if seleccion == 1:
        try:
            cursos = dao.listarCursos()
            if len(cursos)>0:
                funciones.listarCursos(cursos)
            else:
                print("Ocurrio un error no se encontraron cursos")
        except:
            print("Ocurrio un error no se encontraron cursos")
    elif seleccion == 2:
        curso = funciones.datosRegistro()
        try:
            dao.registrarCursos(curso)
        except Error as ex:
            print("No se puede registrar un nuevo curso, intente más tarde", ex)
    elif seleccion == 3:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                curso = funciones.pedirDatosActualizacion(cursos)
                if curso:
                    dao.actualizarCurso(curso)
            else:
                print("No se encontraron cursos con esos parametros para actualizar")
        except Error as ex:
            print("No se puede registrar un nuevo curso, intente más tarde", ex)

    

    elif seleccion == 4:
        try:
            cursos = dao.listarCursos()
            if len(cursos) > 0:
                idEliminar = funciones.pedirDatosEliminacion(cursos)
                if not (idEliminar == ""):
                    dao.eliminarCurso(idEliminar)
                else:
                    print("id de curso no encontrado\n")
            else:
                print("No se encontraron cursos")
        except Error as ex:
            print("No se puede registrar un nuevo curso, intente más tarde", ex)
    else:
        print("Opcion no valida")
menu_principal()

