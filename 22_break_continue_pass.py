#Break: salir de un bucle o estructura repetitiva en cuanto se cumpla una condicion

for numero in range(1, 6):
  if numero == 3:
    break #descanso o interrupcion de una ejecución
  print(f"el numero es {numero}")

print("bucle 1 terminado")

#Continue: omite una parte del bucle cuando se cumple una condicion y continua con el resto

for numero in range(1, 6):
  if numero == 3:
    continue #continuar con el resto del bucle saltando la ejecución actual del mismo
  print(f"el numero es {numero}")

print("bucle 2 terminado")

#pass: permite continuar con una sentencia o función que ya no tiene o aún no tiene un bloque de código útil.

for numero in range(1, 6):
  if numero <= 3:
    #va a repetir el ciclo pasando mientras el numero se mantenga menor o igual a tres, en el momento que se deje de cumplir pasa al else automaticamente y ejecuta ese codigo
    pass
  else:
    print("el siguiente numero es mayor a 3:")
  print(f"el numero es {numero}")

print("bucle 3 terminado")

#También la clausula pass se puede usar cuando se quiere declarar una función pero no ejecutar nada en su interior o cuando tenemos clases vacías sin ejecución todavía
