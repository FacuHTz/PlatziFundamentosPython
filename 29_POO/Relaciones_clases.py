#Relaciones: se puede llamar desde una clase a otra para hacer referencia a una instancia de la misma
#un objeto instanciado a partir de la clase ciudad de la clase ciudad depende de una instancia de la clase país
#En este caso sería imposible usar la clase ciudad sin usar la clase país por lo que podemos decir que depende una de la otra, país se llama a si misma con los parametros, pero ciudad necesita el parametro país para funcionar
class Pais():
  def __init__(self, nom, pre):
    self.nombre = nom
    self.presidente = pre
  def __str__(self):
    txt="País: {0} - Presidente: {1}"
    return txt.format(self.nombre, self.presidente)

class Ciudad():
  def __init__(self, nom, hab, pais):
    self.nombre = nom
    self.habitantes = hab
    self.pais = pais

  def __str__(self):
    txt = f"Ciudad {self.nombre} - Habitantes: {self.habitantes} - {self.pais}"
    return txt

class Barrio():
  def __init__(self, nom, ciu):
    self.nombre = nom
    self.ciudad = ciu
  def __str__(self):
    txt = f"Barrio: {self.nombre} - {self.ciudad}"
    return txt
    

pais1 = Pais("Argentina", "Alberto Fernandez")
print(pais1)
ciudad1 = Ciudad("Buenos Aires", 3000000, pais1)
print(ciudad1)
barrio1 = Barrio("AMBA", ciudad1)
print(barrio1)