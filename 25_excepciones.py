#error en tiempo de ejecucion del programa(durante la ejecucion del programa)

numero1 = 20
numero2 = 0
'''
print(f"la division de {numero1} y {numero2} es {numero1 / numero2}")
#el programa de por si al hacer algo que no se puede tira un error e interrumpe la ejecución del mismo impidiendo que se ejecute el codigo siguiente por más que este bien
'''
#la solucion es encerrarlo en un try/except para que si no llega a ejecutarse un bloque no deje de ejecutarse el resto

try:#ejecuta esto si se puede
  resultado: numero1 / numero2
#except:#ejecuta esto en caso de error del try
except ZeroDivisionError:
  print("no se puede dividir por 0")
finally:#siempre ejecuta esto
  print("siempre se va a ejecutar")

print("aqui continúa el programa normalmente")