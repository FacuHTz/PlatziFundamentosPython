# declarando variables con string
name = "Facundo"
last_name = "Hetze"
my_age= "venticinco"
print(name)
print(last_name)

# concatenando strings
full_name = name + " " + last_name
print(full_name)

# intercambiar entre comillas según las necesidades para no tener errores
quote = "I'm Nicolas"
quote1 = '"holas mis gentes"'
print(quote)
print(quote1)

# formato
# concatenando
template = "Hola mi nombre es " + name + " y mi apellido " + last_name
print(template)

# usando una función
template = "Hola mi nombre es {} y mi apellido {}".format(name, last_name)
print(template)

# usando una función pero solo con la letra f
template = f"Hola mi nombre es {name} {last_name} y mi edad es {my_age}"
print(template)