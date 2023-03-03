#los diccionarios se relacionan con una clave unica, cada elemento se relaciona con una clave, los elementos se almacenan de forma desordenada

miDiccionario = {"España":"Madrid", "Peru":"Lima", "Argentina":"Buenos Aires", "Alemania":"Berlin"}
print(miDiccionario["Peru"])#para leer un elemento necesitamos dar la clave del mismo

miDiccionario["Chile"] = "Santiago de chile"#agregar un elemento al diccionario

miDiccionario["España"] = "Barcelona"#para cambiar/reemplazar el elemento asociado a una clave

#si indicamos una clave nueva se va a agregar un elemento al diccionario pero si usamos la misma clave se va a reemplazar el elemento asociado

del miDiccionario["España"]#para eliminar un elemento del diccionario

miDiccionario2 = {"Facu":"hetze", 25:True, "Sueldo": 150.80 }#los diccionarios permiten asociar tanto en las claves como en los valores distintos tipos de datos

#podemos definir una tupla para definir las llaves

tupla_llaves = ("España", "Argentina", "Peru")
diccionario_tuplas ={tupla_llaves[0]:"Madrid", tupla_llaves[1]:"Buenos Aires", tupla_llaves[2]:"Lima"}
print(diccionario_tuplas)

#se puede definir un diccionario adentro de un diccionario

gustos_helados = {"Nombre":"Facu Hetze", "Gustos Helado":{"gusto1":"Frutilla", "gusto2":"Menta granizada", "gusto3":"Dulce de leche"}}
print(gustos_helados["Gustos Helado"])

#usar el GET en los diccionarios

print(gustos_helados.get("Nombre", "FacuHTz"))#lo que hace es buscar en el diccionario la clave asociada a la palabra Nombre, si no la encuentra va a devolver "FacuHTz" por defecto

print(gustos_helados.keys())#acceder a las llaves unicamente
print(gustos_helados.values())#acceder a los valores unicamente

#se puede almacenar cualquiera de estos valores en listas o en tuplas creando una variable que almacene una lista

valores = list(gustos_helados.keys())
valores = tuple(gustos_helados.keys())