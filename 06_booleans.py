# los booleanos salen de los binarios que son 0 o 1
is_single = True
print(type(is_single),is_single)
is_single = False
print(type(is_single),is_single)

# se puede usar el operador not para cambiar el tipo por su opuesto
print(not True)
print(not False)

is_single = not is_single
print(is_single)