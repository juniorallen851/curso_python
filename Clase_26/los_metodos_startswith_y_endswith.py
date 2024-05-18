"""El método startswith se utiliza para comprobar si una cadena de carácteres
comienza con una subcadena en particulas. 

El método endswith se utiliza para comprobar si una cadena de carácteres
termina con una subcadena en específico.

Además, en ambos métodos es posible establecer un rango de búsqueda dentro de la 
cadena principal.
"""

String = "Diana se peina sola"
resultado = 0
start_swith = "Ejemplos con startswith(): "
end_swith = "Ejemplos con endswith(): "

print (f"\n{start_swith.rjust (50, '=') }")

resultado = String.startswith ("D")
print (f"\n{String} comienza con la subcadena D: {resultado}")

resultado = String.startswith ("d")
print (f"\n{String} comienza con la subcadena d: {resultado}")

resultado = String.startswith ("Diana")
print (f"\n{String} comienza con la subcadena Diana: {resultado}")

resultado = String.startswith ("se", 6)
print (f"\n{String} comienza con la subcadena se, desde la posición 6: {resultado}")

resultado = String.startswith ("se", 6, 7)
print (f"\n{String} comienza con la subcadena se, desde la posición 6 hasta la posición 7: {resultado}")

resultado = String.startswith ("se", 100, 100)
print (f"\n{String} comienza con la subcadena se, desde la posición 100 hasta la posición 100: {resultado}")

resultado = String.startswith ("se", -4, -1)
print (f"\n{String} comienza con la subcadena se, desde la posición -4 hasta la posición -1: {resultado}")


print (f"\n{end_swith.rjust (50, '=') }")

resultado = String.endswith ("A")
print (f"\n{String} termina con la subcadena A: {resultado}")

resultado = String.endswith ("a")
print (f"\n{String} termina con la subcadena a: {resultado}")

resultado = String.endswith ("sola")
print (f"\n{String} termina con la subcadena sola: {resultado}")

resultado = String.endswith ("sola", 10)
print (f"\n{String} termina con la subcadena sola, desde la posición 10: {resultado}")

resultado = String.endswith ("s", 9, 14)
print (f"\n{String} termina con la subcadena s, desde la posición 9 hasta la posición 14: {resultado}")

resultado = String.endswith ("s", 100, 100)
print (f"\n{String} termina con la subcadena s, desde la posición 100 hasta la posición 100: {resultado}")

resultado = String.endswith ("s", -4, -1)
print (f"\n{String} termina con la subcadena s, desde la posición -4 hasta -1: {resultado}")