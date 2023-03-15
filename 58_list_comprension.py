# list conprehension

import math

numeros=[1,4,9,16,25]

raices=[int(math.sqrt(x)) for x in numeros] # Esta linea simplifica todo el proceso de abajo
#La lista interna es asignada a la variable solo cuando todos los elementos fueron ya procesados, es más rapido que el metodo de abajo porque ese va agregando cada vez que recorre el for una instancia a la lista, encambio la otra lo guarda en una memoria interna de python hasta que lo tiene listo y ahí recien lo muestra haciendo que use mucha menos memoria, cuando va creciendo se va a notar el rendimiento
"""
raices=[]
for n in numeros:
    raices.append(int(math.sqrt(n)))
"""

print(raices)

v = [x if (x>10) else "*" for x in numeros] #Acá le añadimos un condicional para que solo imprima x (o sea el lugar de la lista) si este es mayor a 10, sino un * y despues continuamos con el for para recorrerlo a todo normalmente.

print(v)

l=[c.upper() for c in "VientoNorte"] # por cada caracter en viento norte hacer un upper del caracter

print(l)

a = [l if l in "aeiou" else "*" for l in "murcielago"] # por cada l (letra) de la cadena de caracteres "murcielago" ver si cumple con la condicion de adelante que dice que que si l esta en la cadena "aeiou" se muestra sino mostrar un "*"
print(a)