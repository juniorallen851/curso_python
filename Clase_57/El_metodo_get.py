#El método get se utiliza para consultar el valor de de una key en un diccionario 

Diccionario = {"a": 1,
			   "b": 2,
		       "c": 3
		       }

print (f"Diccionario: {Diccionario}")
print()

variable = Diccionario.get("a")
print (variable)

print (f"valor de la key erróneo: {Diccionario.get( 4)}")