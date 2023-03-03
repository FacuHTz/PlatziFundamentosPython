#Paquetes: son directorios o carpetas donde se almacenan modulos relacionados entre sí.
#sirven para organizar mejor el código y reutilizarlo
#para usarlo hay que crear una carpeta con el archivo "__init__.py" dentro y los modulos
#lo que hace __init__ es convertir un directorio en un modulo que contiene otros modulos, esto lo hace para importarlos

from mi_paquete.funciones_numericas import multiplicar
from mi_paquete.funciones_numericas import potenciar

from mi_paquete.funciones_cadena import contarLetras

print(multiplicar(5,8))
print(potenciar(5,8))
print(contarLetras("elusko"))