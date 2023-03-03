def devuelveLenguajes(*lenguajes):#al poner el asterisco se define que se van a pasar una cantidad indeterminada de parametros a la función, además esos parametros se recibiran en forma de tupla.
  for leng in lenguajes:
    yield from leng
#permite almacenar de manera individual los valores dentro de los valores ya almacenados
lenguajesObtenidos = devuelveLenguajes("python", "java", "php", "javascript", "ruby")
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))
print(next(lenguajesObtenidos))