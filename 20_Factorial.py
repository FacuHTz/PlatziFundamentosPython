#Factorial: es el producto de todos los numeros positivos enteros comprendidos entre 1 y el numero especificado

#Factorial de 5: 1 * 2 * 3 * 4 * 5 = 120
#Factorial de 4: 1 * 2 * 3 * 4 = 24

numero = int(input("Ingrese un numero para su factorización: "))#primero pedimos el ingreso de un número por teclado para sacar el factor
factorial = 1
for num in range(1, (numero + 1)):#el for va a recorrer desde el 1 hasta el numero ingresado, recordemos que los rangos siempre llegan a un numero anterior del dado por defecto por eso le sumamos 1
  factorial = factorial * num#acumulamos multiplicaciónes sucesivas 
  #y cuando termina de ejecutarse el for, o sea llega al numero máximo del rango sale con ese resultado acumulado en la variable factorial para imprimirse
print("El factorial de {0} es: {1}".format(numero, factorial))