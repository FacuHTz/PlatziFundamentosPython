#viene de dos prefijos(Poli=> muchas / morfos => formas)
#la finalidad es que un objeto pueda cambiar de forma de acuerdo a su contexto en el cual se ejecuta, y al cambiar su forma tambien cambia su comportamiento.

class Estudiante():
  def describir(self):
    print("Soy un buen estudiante")
class Docente():
  def describir(self):
    print("Soy un buen maestro y todos aprueban")
class Trabajador():
  def describir(self):
    print("Soy un buen Trabajador pero me robo la merienda de mis compañeros")

def describirPersona(persona):
  persona.describir()

doc1=Docente()
describirPersona(doc1)