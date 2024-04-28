print ("\nCalcuadora con una sola variable\n")
print ("================")
print ("Menú de opciones")
print ("================\n")

print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicación")
print ("4. División")
print ("5. División entera")
print ("6. Exponente")
print ("7. Módulo o resto")

opcion = int (input ("\nIntroduce la opción deseada: "))

if opcion == 1:
	print ("Elegiste Suma.\n")

	numero = int (input ("Introduce el primer número: "))
	numero += int (input ("Introduce el segundo número: "))
	print ("El resultado de la suma es: ",numero)

elif opcion == 2:
	print ("Elegiste Resta.\n")

	numero = int (input ("Introduce el primer número: "))
	numero -= int (input ("Introduce el segundo número: "))
	print ("El resultado de la resta es: ",numero)

elif opcion == 3:
	print ("Elegiste Multiplicación.\n")

	numero = int (input ("Introduce el primer número: "))
	numero *= int (input ("Introduce el segundo número: "))
	print ("El resultado de la multiplicación es: ",numero)

elif opcion == 4:
	print ("Elegiste División.\n")

	numero = int (input ("Introduce el primer número: "))
	numero /= int (input ("Introduce el segundo número: "))
	print ("El resultado de la división es: ",numero)

elif opcion == 5:
	print ("Elegiste División entera.\n")

	numero = int (input ("Introduce el primer número: "))
	numero //= int (input ("Introduce el segundo número: "))
	print ("El resultado de la división es: ",numero)

elif opcion == 6:
	print ("Elegiste Exponente.\n")

	numero = int (input ("Introduce el primer número: "))
	numero **= int (input ("Introduce el segundo número: "))
	print ("El resultado del Exponente es: ",numero)

elif opcion == 7:
	print ("Elegiste Módulo o resto.\n")

	numero = int (input ("Introduce el primer número: "))
	numero %= int (input ("Introduce el segundo número: "))
	print ("El resultado del módulo o resto es: ",numero)

else:
	print ("opción no válida.")



