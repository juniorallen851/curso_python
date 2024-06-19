Diccionario = {"a": 1,
			   "b": 2,
		       "c": 3
		       }

print (Diccionario)
print (f"\nLos items del Diccionario son:\n{Diccionario.items()}")

print (f"\nConvirtiendo items a lista")
list_items = list(Diccionario.items())

print(f"La lista es: {list_items}")
print (f"Posición 1 de la lista items: {list_items[1]}")