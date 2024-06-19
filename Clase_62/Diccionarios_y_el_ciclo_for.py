Diccionario = {"a": 1,
			   "b": 2,
		       "c": 3
		       }

# Recorriendo únicamente las claves:

for key in Diccionario:
	print (f"{key} : {Diccionario[key]}")
print ()

# Recorriendo los items:

for key, value in Diccionario.items():
	print (f"{key} : {value}")
