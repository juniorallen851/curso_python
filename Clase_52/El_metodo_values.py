Diccionario = {"a": 1,
			   "b": 2,
		       "c": 3
		       }

print (Diccionario)
print (f"\nLos valores del Diccionario son:\n{Diccionario.values()}")

print (f"\nConvirtiendo valores a lista")
list_valores = list(Diccionario.values())

print(f"La lista es: {list_valores}")
print (f"Posición 1 de la lista keys: {list_valores[1]}")