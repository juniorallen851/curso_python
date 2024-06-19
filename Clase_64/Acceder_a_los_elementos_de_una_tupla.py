"""Para acceder a los elementos de una tupla existen 3 alternativas para hacerlo:

1- Mediante índices.
2-Mediante el operador de segmentación.
3-Mediante el desempaquetado de tuplas"""

# Ejemplo mediante índices

print ("\nAccediendo a los elementos de tuplas de tuplas a través de índices.")

tupla_heterogenea = (3, True, "hola", 2.5)
print ()
print (tupla_heterogenea)
print ()

print (f"Elemento booleano de la tupla heterogenea: {tupla_heterogenea [1]}\n")

# Mediante el operador de segmentación

print ("Operador de segmentación.\n")

print (f"Segundo y tercer elemento de la tupla: {tupla_heterogenea [1: 3]}")
print (f"Todos los elementos de la tupla de dos en dos: {tupla_heterogenea [:: 2]}\n")

# Mediante el desempaquetado de tuplas

print ("Desempaquetado de tuplas.\n")

variable_1, variable_2, variable_3, variable_4 = tupla_heterogenea[::]
print (variable_1, variable_2, variable_3, variable_4)