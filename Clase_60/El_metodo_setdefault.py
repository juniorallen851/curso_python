"""El método setdefault es un metodo de diccionarios. Este método se
utiliza para asignar un valor a una clave en un diccionario si la clave
no existe ya en el diccionario.

 Si la clave ya existe en el diccionario, el método setdefault devuelve
 el valor correspondiente a esa clave.

 y si la clave no existe, el método crea la clave con el valor específicado
 y devuelve ese valor."""

Diccionario = {"a": 1,
			   "b": 2,
		       "c": 3
		       }

print (f"Diccionario original: {Diccionario}")		       
print ()

Diccionario.setdefault("d", 4)

print (f"Diccionario actual: {Diccionario}")