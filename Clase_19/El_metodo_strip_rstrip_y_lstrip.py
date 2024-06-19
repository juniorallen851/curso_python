""" ejemplo strip (el strip elimina carácteres de una cadena de carácteres al inicio
 de la cadena y al final (incluso los espacios, los saltos de línea \n y tabulación \t))

 Para eliminar espacios simplemente hay que dejar los parentesis de el strip, lstrip o 
 rstrip vacios"""

cadena = "Ender de minecraft"
print (cadena)

cadena = cadena.strip("Ent")
print (cadena)

"""el strip al eliminar un carácter vuelve a evaluar los carácteres asignados de inicio a
fin hasta que no encuentre mas carácteres que eliminar."""

#\t = tabulación (       minecraft)

"""ejemplo rstrip (Se utiliza solo para eliminar carácteres específicos al final de una
cadena de carácteres)"""

cadena_1 = "Ender de minecraft"

cadena_1 = cadena_1.rstrip("Etfra")
print (cadena_1)

"""ejemplo lstrip (Se utiliza solo para eliminar carácteres específicos al inicio de una
cadena de carácteres)"""

cadena_2 = "Ender de minecraft"

cadena_2 = cadena_2.lstrip("Edn")
print (cadena_2)