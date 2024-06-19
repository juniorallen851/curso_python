Diccionario = {"a": 1,
			   "b": 2,
		       "c": 3
		       }

print (Diccionario)
print (f"\nLas keys del Diccionario son:\n{Diccionario.keys()}")

print (f"\nConvirtiendo keys a lista")
list_keys = list(Diccionario.keys())

print(f"La lista es: {list_keys}")
print (f"Posición 1 de la lista keys: {list_keys[1]}")