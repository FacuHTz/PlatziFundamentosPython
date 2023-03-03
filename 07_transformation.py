# se puede cambiar el tipo de dato en cualquier momento y python lo infiere automaticamente
name = "Nicolas"
print(type(name))
name = 12
print(type(name))
name = True
print(type(name))

# hay que tener en cuenta la diferencia entre sumar y concantenar porque el operador + hace las dos cosas
print("Facundo" + " Hetze")
print(10 + 20)

# hay que tener cuidado de no mandarle dos tipos distintos de datos para combinar porque no puede Python
# print("Facundo" + 12) no se puede hacer
# lo que hay que hacer es cambiarle el tipo, se puede hacer de cualquier de las dos formas

age = 12
print("Mi edad es " + str(age))#aca se lo decimos explicitamenete
print(f"Mi edad es {age}")#acá lo detecta automaticamente

# tambien se puede cambiar el tipo de string a int
age = input("Escribe tu edad > ")
print(type(age))
new_age = int(age) + 10
print(f"Tu edad en 10 años será {new_age}")
