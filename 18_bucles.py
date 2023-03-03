#son estructuras de control de flujo que repiten 1 o varias lineas de codigo.
for num in range(0, 20, 2):
  print("valor actual {0}".format(num))

for i in range(1, 13):
  print("{0} x {1} es: {2}".format(i, i, (i * i)))

for nom in ["Facu", "Tano", "Belen", "Chelo", "Nico"]:
  print("Cantidad de letras de {0} es {1}".format(nom, len(nom)))