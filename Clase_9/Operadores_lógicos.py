#Conjunción

print ("Conjunción (and)")

numero_uno = int (input ("Escribe un número que sea menor que 10 y mayor que 5: "))

if numero_uno < 10 and numero_uno > 5:
	print ("\nEl número", numero_uno, "cumple con la condición. \n")

else:
	print ("\nEl número", numero_uno, "no cumple con la condición. \n")

#Disjunción

print ("Disjunción (or)")

palabra = input ('Para cumplir la condición escribe "si" o "yes": ')
palabra = palabra.lower()

if palabra == "si" or palabra == "yes":
	print ("\nLa condición se ha cumplido. \n")

else:
	print ("\nLa condición no se ha cumplido.\n")

#Negación

print ("Negación (not)")

numero_2 = int (input ('Introduce un número igual a "5": '))

if not numero_2 == 5:
	print ("\nEl número es diferente de 5 y SI cumple la condición.\n")

else:
    print ("\n El número es igual a 5 y NO cumple la condición.")	






