"""El método copy se utiliza para crear una copia de un objeto,como listas
matrices o diccionarios."""

Diccionario = {"a": 1,
			   "b": 2,
		       "c": 3
		       }

print (f"Diccionario : {Diccionario.items()}")
print ()

Diccionario_copia = Diccionario.copy()

print (Diccionario)