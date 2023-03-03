#Los constructores se usan para dar valores a los objetos de forma dinamica

class Curso():
  # nombre = "Matematicas"
  # creditos = 5
  # carrera = "Ingeniería Civil"
  def __init__(self, nom, cre, car):
    self.nombre = nom
    self.creditos = cre
    self.carrera = car
    self.__imparticion = "Presencial" #propiedad encapsulada(no se puede acceder a ella desde afuera de la clase)
  def mostrarCursos(self):
    dat = "curso: {0}, creditos: {1}, modo de imparticion: {2}"
    print(dat.format(self.nombre, self.creditos, self.__imparticion))
    docenteAsignado = self.__verificarDocente()
    if docenteAsignado:
      print("Docente asignado")
    else:
      print("No hay docente asignado")

  #funcion o metodo de clase encapsulada
  def __verificarDocente(self):
    print("Verificando si existe un docente asignado...")
    if self.__imparticion == "Presencial":
      return True
    else:
      return False

  #es una funcion que devuelve en forma de string los datos de una instancia o clase
  def __str__(self):
    texto = "curso: {0} - creditos: {1}"
    return texto.format(self.nombre, self.creditos)

curso1 = Curso("Matematicas", 5, "Ingeniería Civil")
print("curso1.nombre")
curso2 = Curso("Fisica", 2, "Ingeniería Civil")
print("curso1.nombre")
curso1.mostrarCursos()