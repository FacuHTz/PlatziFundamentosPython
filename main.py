import random

opcion_aleatoria = random.choice(["piedra", "papel", "tijera"])

print("Piedra, papel o tijeras game")
user_option = input("elige una opcion > ")
computer_option = opcion_aleatoria

print("la pc eligió " + computer_option)

if user_option == computer_option:
  print("empataste con la pici")
elif user_option == "piedra":
  if computer_option == "tijera":
    print("piedra gana a tijera")
    print("gano el usuario")
  else:
    print("papel gana a piedra")
    print("computer gano")
elif user_option == "papel":
  if computer_option == "piedra":
    print("papel gana a piedra")
    print("user gana")
  else:
    print("tijera gana a papel")
    print("computer wins")
elif user_option == "tijera":
  if computer_option == "papel":
    print("tijera gana a papel")
    print("user wins")
  else:
    print("piedra gana a tijera")
    print("computer wins this battle")