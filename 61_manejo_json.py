import json
# Si tenemos un string de JSON con estas caracteristicas podemos pasarlo a un diccionario de Python facilmente
"""
json_str='{"nombre":"Oscar", "edad":28, "pais":"Argentina"}'
print(json_str)
print(type(json_str))

python_dict = json.loads(json_str)
print(python_dict)
print(type(python_dict))
print(python_dict['pais'])
print(python_dict['edad'])
"""

"""
data = {
    "empresa":"NorteGAS",
    "duenio":"Jose",
    "edad":50,
    "hijos":["facu","brenda"]
}

json_data = json.dumps(data)
print(json_data)
print(type(data))
"""

"""
Equivalencias
Python  |   JSON
dict    =>  Object
list    =>  Array
tuple   =>  Array
str     =>  String
int     =>  Number
float   =>  Number
True    =>  true
False   =>  false
None    =>  null

"""
"""

data = {
    "empresa":"NorteGAS",
    "duenio":"Jose",
    "edad":50,
    "hijos":["facu","brenda"]
}

json_data = json.dumps(data, indent=4, separators=(", "," : "), sort_keys = True)
print(json_data)
"""
"""
json_data = json.JSONEncoder().encode({"lenguejes":["python","JavaScript"]})
print(json_data)
print(type(json_data))

python_dict = json.JSONDecoder().decode(json_data)
print(python_dict)
print(type(python_dict))
"""
class Curso():
    def __init__(self, codigo,nombre,creditos):
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos

curso_1 = Curso("132342", "Lengueje", 4)

json_object_data = json.dumps(curso_1.__dict__)
print(json_object_data)
print(type(json_object_data))

python_dict = json.loads(json_object_data)
print(python_dict)
print(type(python_dict))