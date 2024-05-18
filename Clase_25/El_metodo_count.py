"""El método count es de gran utilidad cuando se necesita conocer la cantidad de
veces que aparece una cadena, subcadena o carácter en específico dentro de un
texto.

Además, también tiene la capacidad de buscar una subcadena en una parte en 
específico de la cadena principal."""

String = "Mi mamá me mima"
contador = 0

print (String.center(40, "="))

contador = String.count("M")
print (f"\nLa letra M se encontró {contador} veces en la cadena: {String}")

contador = String.count("m")
print (f"\nLa letra m se encontró {contador} veces en la cadena: {String}")

contador = String.count("mamá")
print (f"\nLa palabra mamá se encontró {contador} veces en la cadena: {String}")

contador = String.count("me mima")
print (f"\nLa oración me mima se encontró {contador} veces en la cadena: {String}")

contador = String.count("ma")
print (f"\nLa palabra ma se encontró {contador} veces en la cadena: {String}")

contador = String.count("m", 13)
print (f"\nLa letra m se encontró {contador} veces desde la posición 13 en la cadena: {String}")

contador = String.count("m", 100)
print (f"\nLa letra m se encontró {contador} veces desde la posición 100 en la cadena: {String}")

contador = String.count("m", -3)
print (f"\nLa letra m se encontró {contador} veces desde la posición -3 en la cadena: {String}")

contador = String.count("m", 3, 7)
print (f"\nLa letra m se encontró {contador} veces desde la posición 3 hasta la posición 7 en la cadena: {String}")

contador = String.count("m", 100, 100)
print (f"\nLa letra m se encontró {contador} veces desde la posición 100 hasta la posición 100 en la cadena: {String}")

contador = String.count("m", -4, -1)
print (f"\nLa letra m se encontró {contador} veces desde la posición -4 hasta la posición -1 en la cadena: {String}")