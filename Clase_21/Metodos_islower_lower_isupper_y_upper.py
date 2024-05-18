"""#1

El método islower se utiliza para identificar si todas las letras de una
cadena de carácteres se encuentran en minúsculas y el método lower convierte
todas las letras de una cadena de carácteres en minúsculas.

#2 

El método isupper se utiliza para saber si todas las letras de una cadena de 
carácteres estan en mayúsculas y upper se encarga de convertir todas las letras
de una cadena de carácteres en mayúsculas. 

#3

El método islower y isupper dan su respuesta con un valor booleano (True-False).

"""

String = input ("introduce un String: ")

print (f"\n¿Todas las letras estan en minúsculas?: {String.islower ()}")
String = String.lower ()
print (f"String en minúsculas: {String}")

print (f"¿Todas las letras estan en mayúsculas?: {String.isupper ()}")
print (f"String en mayúsculas: {String.upper()}")
print (f"String original: {String}")