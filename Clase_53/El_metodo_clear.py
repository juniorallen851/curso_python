# El metodo clear se utiliza para eliminar todos los elementos de un objeto
#Estos pueden ser una lista, un diccionario o un conjunto 

Diccionario = {"a": 1,
			   "b": 2,
		       "c": 3
		       }

print("Elementos del Diccionario.")
print (Diccionario.items())

print ("\nDiccionario después aplicar el metodo clear.\n")

Diccionario.clear()
print (Diccionario)