print ("Sistema para calcular el promedio de un alumno.")

nombre = input ("Para comenzar escribe tu nombre: ")
matematicas = int ( input (nombre + " ¿Cuál es tu calificación en matemáticas?: "))
quimica = int ( input (nombre + " ¿Cuál es tu calificación en química?: "))
biologia = int ( input (nombre +" ¿Cuál es tu calificación en biología?: "))

promedio = (matematicas + quimica + biologia) // 3

if promedio >= 6:
	print ('Felicidades ' + nombre + ' "aprobaste" con un promedio de:',promedio)
else:
	print ( nombre + ' Lamentablemente tu promedio no es suficiente, has reprobado con un promedio de:',promedio)

print ("Eso es todo")

"""Las sentencias condicionales simples son las que no ejecutan nada si la condición
no se cumple, sin embargo, las que si ejecutan una instrucción si no se cumple la 
condición son sentencias condicionales compuestas"""

#Sentencia condicional multiple

print ("===============================")
print ("Convertidor de números a letras")
print ("===============================")

número = int (input ("¿Cuál es el número que deseas Convertir?: "))

if número == 1:
	print ('el número es "UNO"')

elif número == 2:
	print ('el número es "DOS"')

elif número == 3:
	print ('el número es "TRES"')

elif número == 4:
	print ('el número es "CUATRO"')

elif número == 5:
	print ('el número es "CINCO"')

else:
	print ('Este convertidor solo puede convertir hasta el número "5"')

print ("Fin.")

# Sentencia condicional anidada

print ("===========")
print ("Convertidor")
print ("=========== \n")

print ("Menú de opciones. \n")
print ("Presine la tecla 1 si desea covertir un número a palabra.")
print ("Presine la tecla 2 si desea covertir una palabra a letra. \n")

opción = int(input("¿Cuál es su opción deseada?:") )

if opción == 1:
	número_1 = int(input("\n¿Cuál es el número que desea covertir?: "))

	if número_1 == 1:
		print ('El número es "UNO"')

	elif número_1 == 2:
		print ('El número es "DOS"')

	elif número_1 == 3:
		print ('El número es "TRES"')

	elif número_1 == 4:
		print ('El número es "CUATRO"')

	elif número_1 == 5:
		print ('El número es "CINCO"')

	else:
		print ("El número seleccionado no esta registrado.")

elif opción == 2:
	número_1 = input("\n¿Cuál es el número que desea covertir?: ")
	número_1 = número_1.lower ()

	if número_1 == "uno":
		print ('El número es "1"')

	elif número_1 == "dos":
		print ('El número es "2"')

	elif número_1 == "tres":
		print ('El número es "3"')

	elif número_1 == "cuatro":
		print ('El número es "4"')

	elif número_1 == "cinco":
		print ('El número es "5"')

	else:
		print ("El número seleccionado no esta registrado.")

else:
	print ("Opción no encontrada")
	print ("Fin.")