#sirve para ejecutar de forma intencional excepciones en python.
#al ejecutar un error a proposito se logra a detención del programa y no sigue ejecutandose

def evaluarNota(nota):
  if nota < 0:
    # raise ZeroDivisionError("no se permiten valores negativos")
    raise ValueError("valor incorrecto")
    #print("nota no valida")
  elif nota >= 10:
    print("excelente")
  elif nota >= 6:
    print("aprobado")
  else:
    print("desaprobado")

evaluarNota(-2)