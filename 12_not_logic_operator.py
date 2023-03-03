print(not True)
print(not False)

# not
print("NOT AND")
print("not True and True >", not(True and True))
print("not True and False >", not(True and False))
print("not False and True >", not(False and True))
print("not False and False >", not(False and False))

print("*"*20)

stock = input("ingrese el numero de articulos en stock > ")
stock = int(stock)
print(not(stock >= 100 and stock <=1000))#encerrando toda la operación dentro de un not da el resultado opuesto al que daría si no tuviera el not

print("*"*20)