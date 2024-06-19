print ()
print (" ----------------------")
print ("| El número más grande |")
print (" ----------------------")

print ()
numero_1 = float (input ("Ingresa el primer número: "))
numero_2 = float (input ("Ingresa el segundo número: "))
numero_3 = float (input ("Ingresa el tercer número: "))
print ()


if numero_1 > numero_2:
	if numero_1 > numero_3:
		print (f"El número {numero_1} es el número más grande.")

if numero_2 > numero_1:
	if numero_2 > numero_3:
		print (f"El número {numero_2} es el número más grande.")

if numero_3 > numero_1:
	if numero_3 > numero_2:
		print (f"El número {numero_3} es el número más grande.")

if numero_1 == numero_2:
	if numero_1 == numero_3:
		print ("Todos los números son iguales.")