# Secuencia con lista sin valor asignado

Secuencia = ["uno", "dos", "tres"]
dicc_name = dict.fromkeys (Secuencia)
print ("Secuencia con lista sin valor:", dicc_name)

# Secuencia con lista con valor asignado

Secuencia = ["uno", "dos", "tres"]
valor = 5
dicc_name = dict.fromkeys(Secuencia, valor)

#Secuencia con Diccionario

Secuencia = {"a": 1,
			 "b": 2,
		     "c": 3
		      }

valor = 5
dicc_name = dict.fromkeys(Secuencia, valor)
print ("Secuencia con diccionario y valor:",dicc_name)

# Secuencia con texto

dicc_name = {}.fromkeys("hola", 1)
print ("Secuencia con texto y valor:", dicc_name)