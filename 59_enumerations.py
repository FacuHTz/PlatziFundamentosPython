from enum import Enum

class Color(Enum):
     rojo="#ff0000"
     verde="#008000"
     azul="#0000ff"
 
print(Color.rojo.value)
print(Color("#0000ff"))
print(Color["rojo"].value)

"""
lista1=[]
for c in Color:
    lista1.append(c)

print(lista1)
"""

lista = [c for c in Color]
print(lista)