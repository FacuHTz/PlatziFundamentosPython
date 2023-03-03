class Persona():
  #propiedades, caracteristicas o atributos
  apellidos=""
  nombres=""
  edad=0
  despierta=False

  #Funcionalidades
  def despertar(self):
    #self es una palabra reservada que hace referencia al la instancia u objeto perteneciente a la clase
    self.despierta = True
    print("Buen día")

persona1 = Persona()


persona1.nombres = "Facu"
print(persona1.nombres)
# persona1.despertar()
# print(persona1.despierta)
persona1.apellodos = "Hetze seip"
print(persona1.apellidos)