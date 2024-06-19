print ()
print ("Calculadora\n")

print (" ----------------------------------") 
print ("| Seleccione la operación deseada: |")
print (" ----------------------------------\n") 

print ("1. Suma.")
print ("2. Resta.")
print ("3. Multiplicación.")
print ("4. División.")
print ("5. División Entera.")
print ("6. Exponente.")
print ("7. Módulo o Resto.")

numero = int (input ("\nAsigne el número de la operación que desee: "))

if numero == 1:
	print ("\nSuma.")

	numero = int (input ("\nIngresa el primer número: "))
	numero += int (input ("Ingresa el segundo número: "))

	print (f"El resultado de la suma es: {numero}")

elif numero == 2:
	print ("\nResta.")

	numero = int (input ("\nIngresa el primer número: "))
	numero -= int (input ("Ingresa el segundo número: "))

	print (f"El resultado de la resta es: {numero}")

elif numero == 3:
	print ("\nMultiplicación.")

	numero = int (input ("\nIngresa el primer número: "))
	numero *= int (input ("Ingresa el segundo número: "))

	print (f"El resultado de la multiplicación es: {numero}")

elif numero == 4:
	print ("\nDivisión.")

	numero = int (input ("\nIngresa el primer número: "))
	numero /= int (input ("Ingresa el segundo número: "))

	print (f"El resultado de la división es: {numero}")

elif numero == 5:
	print ("\nDivisión Entera.")

	numero = int (input ("\nIngresa el primer número: "))
	numero //= int (input ("Ingresa el segundo número: "))

	print (f"El resultado de la división entera es: {numero}")

elif numero == 6:
	print ("\nExponente.")

	numero = int (input ("\nIngresa el primer número: "))
	numero **= int (input ("Ingresa el segundo número: "))

	print (f"El resultado del exponente es: {numero}")

elif numero == 7:
	print ("\nMódulo o Resto.")

	numero = int (input ("\nIngresa el primer número: "))
	numero %= int (input ("Ingresa el segundo número: "))

	print (f"El módulo o resto es: {numero}")

else:
	print ("\nEl número que ingresó no se encuentra en la lista.")