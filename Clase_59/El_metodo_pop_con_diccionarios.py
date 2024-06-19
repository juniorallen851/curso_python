Diccionario = {"a": 1,
			   "b": 2,
		       "c": 3
		       }

print (f"Diccionario original: {Diccionario}")
valor = Diccionario.pop("b")

print (f"Diccionario modificado: {Diccionario}")
print (f"Valor eliminado: {valor}")

print ()
Diccionario = {"a": 1,
			   "b": 2,
		       "c": 3
		       }

print (f"Diccionario original:{Diccionario}")
valor = Diccionario.pop("z", "No se encuentra la clave dentro del diccionario.")

print (f"Diccionario modificado : {Diccionario}")
print (f"Valor eliminado: {valor}")