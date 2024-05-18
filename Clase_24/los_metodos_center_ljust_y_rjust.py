"""En python es posible alinear el texto que se imprime en pantalla de distintas
formas, con estos tres métodos se puede alinear una impresión en pantalla a la 
izquierda, a la derecha o al centro.

center = centro
ljust = izquierda
rjust = derecha

estos métodos colocan espacios o carácteres (según un prefiera) para lograr 
colocar el String en el lugar que se indique.
"""

String = "Menú"

print ("Métodos con espacios: ")
print (String.center(20))
print (String.ljust (20))
print (String.rjust (20))

print ("Métodos con caracter:")
print (String.center (20, "="))
print (String.ljust (20, "="))
print (String.rjust (20, "="))

print ("\nVariable modificada:")
String = String.center (10, "=")
print (String)