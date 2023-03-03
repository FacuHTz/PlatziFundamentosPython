#range(): Crea una lista inmutable de numeros enteros en sucesion aritmetica.

numeros = range(5)#[0, 1, 2, 3, 4]
print(numeros[3])

numeros = range(4, 10)#[4, 5, 6, 7, 8, 9]
print(numeros[5])# acá puedo usar del 0 al 5 para referirme a los valores dentro del rango

numeros = range(10, 100, 8)#a este rango se le especifica que dentro de ese rango, de 0 a 100 tienen que ir aumentando de 8 en 8
print(numeros[4])#Los posibles resultados[10, 18, 26, 34, 42, 50, 58, 66, 74, 82, 90, 98]
