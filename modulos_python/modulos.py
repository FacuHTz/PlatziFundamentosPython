# Importacion de un módulo que se encuentra en la misma ruta:
# Asi importamos el archivo solamente pero no cada funcion, por lo tanto tenemos que llamar a cara funcion a traves de el archivo:
"""
import modulos1
print(modulos1.multiplicar(7,8))
print(modulos1.sumar(7,8))
print(modulos1.dividir(7,8))
print(modulos1.restar(7,8))
"""

# Así importamos directamente las funciones para poder usarlas sin necesidad de nombrar el archivo adelante:
"""
from modulos1 import sumar, restar, dividir, multiplicar, negocio

print(multiplicar(19, 2))
print(sumar(19, 2))
print(restar(19, 2))
print(dividir(19, 2))
print(negocio)

"""
#importación desde un paquete:
"""
from mi_paquete.operaciones_matematicas import calcular_factorial
print(calcular_factorial(5))
"""
#importación desde un paquete: (acá con la palabra import tenemos que llamar todo desde el print cuando queremos ejecutar la operación)
"""
import mi_paquete.operaciones_matematicas
print(mi_paquete.operaciones_matematicas.calcular_factorial(5))
"""

#importación desde un paquete: (usando un alias)
"""
import mi_paquete.operaciones_matematicas as fun_mat
print(fun_mat.calcular_factorial(5))
"""
#importación de un subpaquete:
"""
from mi_paquete.sub_paquete1.funciones_avanzadas import contar_letras
texto="nortegas"
print(contar_letras(texto))
"""