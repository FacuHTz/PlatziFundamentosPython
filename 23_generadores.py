#Los generadores nos permiten extraer valores de una función y almacenarlo de uno en uno en objetos iterables(que se pueden recorrer) sin la necesidad de almacenar todos a la vez en la memoria RAM.

#acá hicimos una función que genera una lista con todos los multiplos de 7 y el limite se lo definimos nosotros
"""
def generaMultiplos7(limite):
  numero = 1
  listaNumeros = []

  while numero <= limite:
    listaNumeros.append(numero*7)
    numero=numero+1
  return listaNumeros

print(generaMultiplos7(10))
"""

#acá lo hicimos con un generador en el que quedaron guardadas las propiedades resultantes

def generaMultiplos7(limite):
  numero = 1

  while numero <= limite:
    yield numero * 7 #la instruccion yield genera un objeto iterable
    numero += 1

obtieneMultiplos7 = generaMultiplos7(10)

print(obtieneMultiplos7)
for n in obtieneMultiplos7:
  print(n)

#se puede usar para iterar con el objeto la función next(): que retorna el siguiente elemento de un objeto iterable

print(next(obtieneMultiplos7))
print(next(obtieneMultiplos7))
#se pueden tener las lineas de código que se quieran en el medio que siempre se va a poder iterar de uno en uno el objeto almacenado en un generador
#los generadores son más eficientes que las funciones tradicionales para trabajar con listas y son muy utiles con listas de valores infinitos, nos puede mostrar los vlaores uno por uno y no toda una lista de valores infinitos que serían imposibles de trabajar de otra forma 
#entre llamada y llamada el objeto iterable entra en pausa(estado de suspensión)
print(next(obtieneMultiplos7))

