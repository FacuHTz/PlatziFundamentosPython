x = 3.3
print(x)
y = 1.1 + 2.2
print(y)
print(x == y) #false porque dan una precisión decimal distinta al procesarlos en la pc

y_str = format(y, ".2g") #lo pasamos a string
print(y_str == str(x)) #true pero de forma string

print("*" *10)#linea divisoria

print(y, x)

tolerance = 0.00001 #tolerancia/margen de error que podemos poner para tener un rango en el que no afecte al funcionamiento del programa si es ligeramente distinto
print(abs(x -y) < tolerance) #true pero por via matematica, lo que se hace es restarse entre los dos y si la diferencia es menor a la tolerancia aceptada entonces es verdadero