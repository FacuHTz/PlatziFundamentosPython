class ClaseA():
  def __init__(self, par1, par2):
    self.parametro1 = par1
    self.parametro2 = par2
    

class ClaseB():
  def __init__(self, par3, par4, par5):
    self.parametro3 = par3
    self.parametro4 = par4
    self.parametro5 = par5

class ClaseX(ClaseA,ClaseB):
  pass

cX1=ClaseX(12, 13)
#Cuando en una clase llamamos como herencia dos clases más solo toma por defecto la primera clase, al pasarle los parametros vemos que solo nos pide los de ClaseA, no los de ClaseB, y si le pasamos parametros para todas las clases tira error, solo le importan los parametros de la primera clase
