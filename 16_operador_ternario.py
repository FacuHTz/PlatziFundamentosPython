#en cualquier lenguaje de programación un operador ternario se haría de la siguiente forma:
#sexo = (10 > 20) ? "Masculino" : "Femenino"
#el operador ternario sirve para evaluar facilmente una condición y en respuesta a eso asignar uno de los dos resultados posibles

#en python podemos simularlo de la siguiente manera

sexos = ("Masculinto", "Femenino")

posicion = True
sexo = sexos[posicion]
print(sexo)
sexo = sexos[not posicion]
print(sexo)
#lo que hacemos es asignarle un valor booleano a cada valor de nuestra tupla, entonces la primera posicion esta obligada a ser 0 y la siguiente a ocupar el espacio que le quede o sea 1