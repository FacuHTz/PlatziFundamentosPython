class Persona():

  def __init__(self, apePat, apeMat, nom):
    self.apellidoPaterno = apePat
    self.apellidoMaterno = apeMat
    self.nombres = nom

  def mostrarNombreCompleto(self):
    txt = "{0} {1}, {2}"
    return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

    
class Estudiante(Persona):#si bien es otra clase dado que se pasa como parametro la clase anterior, esta puede acceder a todos los metodos de la otra sin necesidad de reescribir nada.
  def __init__(self, pro, apePat, apeMat, nom):
    super().__init__(apePat, apeMat, nom)
    self.profesion = pro



estudiante1 = Estudiante("Torres", "Lopez", "Nicolas", "Medico")
persona1 = Persona("Torres", "Lopez", "Nicolas")
# print(estudiante1.mostrarNombreCompleto())

print(isinstance(estudiante1, Persona))