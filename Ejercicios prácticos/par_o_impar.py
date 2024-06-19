print ("--------------------------------------------------------")
print ("| Programa para determinar si un número es par o impar |")
print ("--------------------------------------------------------")

numero = int (input ("Ingresa un número: "))
print ("")

divisor = 2
resultado = numero % divisor

print (resultado)

if resultado == 0:
	print (f"\nEl número {numero} es par.")
else:
	print (f"\nEl número {numero} es impar.")