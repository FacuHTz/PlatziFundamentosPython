# AND
print("AND")
print("True and True >", True and True)
print("True and False >", True and False)
print("False and True >", False and True)
print("False and False >", False and False)
print("*"*20)
print(10 > 5 and 5 < 10)
print(10 < 5 and 5 > 10)
print("*"*20)

stock = input("ingrese el numero de articulos en stock > ")
stock = int(stock)
print(stock >= 100 and stock <=1000)#esto vendría a ser una regla en la cual se va a evaluar si hay más de 100 o menos de 1000 articulos, en ese caso va a ser true, sino va a ser false
print("*"*20)


# OR
print("OR")
print("True or True >", True or True)
print("True or False >", True or False)
print("False or True >", False or True)
print("False or False >", False or False)
print("*"*20)

role = input("digita el rol > ")
print(role=="admin" or role == "seller")#va a devolver un valor booleano de acuerdo a lo ingresado en el input, cualquiera de las dos, tanto admin como seller van a poder ingresar

print("*"*20)