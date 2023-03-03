#es u archivo con extension py o pyc(python compilado) es un archivo que posee su propio espacio de nombres y puede contener variables, funciones, clases o hasta otros modulos
#los modulos sirven para organizar el codigo y reutilizarlo
#Modularizacion y Reutilizacion

import funciones_matematicas#así se importa un archivo
print(funciones_matematicas.multiplicar(5,6))


from Files.modulos.funciones_matematicas import sumar#así se importan directamente las funciones del archivo para no tener que llamar al archivo cada vez que ejecutemos la función, tambien se puede importar con un * para que traiga todas las funciones
print(sumar(5,6))
