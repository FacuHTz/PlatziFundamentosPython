def listarCursos(cursos):
    print("\nCursos: \n")
    count = 1
    for cur in cursos:
        datos = f"{count}. codigo: {cur[0]} | Asignatura: {cur[1]} (creditos: {cur[2]})"
        print(datos)
        count = count + 1
print(" ")

def datosRegistro():
    idCorrecto = False
    while (not idCorrecto):
        idCurso = input("Escriba el ID del curso: ")
        if len(idCurso) == 6:
            idCorrecto = True
        else:
            print("Verifique el codigo ingresado e intentelo de nuevo")

    nombre = input("Ingrese el nombre del curso: ")
    creditoCorrecto = False
    while (not creditoCorrecto):
        creditos = input("ingrese los creditos del curso: ")
        if creditos.isnumeric():
            if (int(creditos)>0):
                creditoCorrecto = True
                creditos = int(creditos)
            else:
                print("Verifique los creditos ingresados e intentelo de nuevo")
        else:
            print("Verifique los creditos ingresados e intentelo de nuevo")

    curso = (idCurso, nombre, creditos) 
    return curso

def pedirDatosActualizacion(cursos):
    listarCursos(cursos)
    existeId = False
    idActualizar=int(input("Ingrese el código del curso a Actualizar: "))
    for cur in cursos:
        if cur[0] == idActualizar:
            existeId=True
            break

    if existeId:
        nombre = input("Ingrese el nombre del curso: ")
        creditoCorrecto = False
        while (not creditoCorrecto):
            creditos = input("ingrese los creditos del curso: ")
            if creditos.isnumeric():
                if (int(creditos)>0):
                    creditoCorrecto = True
                    creditos = int(creditos)
                else:
                    print("Verifique los creditos ingresados e intentelo de nuevo")
            else:
                print("Verifique los creditos ingresados e intentelo de nuevo")
        curso = (idActualizar, nombre, creditos)
    else:
        curso = None
    
    
    return curso


def pedirDatosEliminacion(cursos):
    listarCursos(cursos)
    existeId = False
    idEliminar=input("Ingrese el código del curso a eliminar: ")
    for cur in cursos:
        if cur[0] == idEliminar:
            existeId=True
            break
    if not existeId:
        idEliminar == ""
    
    return idEliminar