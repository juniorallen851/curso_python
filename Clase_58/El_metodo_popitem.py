"""El método popitem se utiliza para eliminar el último elemento de un 
diccionario (Clave-Valor)

este elemento no es eliminado del todo, puede se almacenado tempralmente
en una variable."""

Diccionario = {"a": 1,
			   "b": 2,
		       "c": 3
		       }

ultimo_item = Diccionario.popitem()
print (Diccionario, "\n", ultimo_item)