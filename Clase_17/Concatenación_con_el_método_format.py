nombre = "Alejandro"
edad = 23

print ("Hola {} tienes {} años.".format(nombre,edad))

"""El método format para concatenar cadenas de carácteres puede concatenar cadenas 
de carácteres con valores entero sin necesidad de utilizar el srt"""

# 2da forma de utilizar el método format

print ("Hola {nom_1} tienes {edad_1} años.".format (nom_1 = "Carmen", edad_1 = 50))

# 3ra y última forma de utilizar el método format

nombre_2 = "Aura"
edad_2 = 40

print ("Hola {1} tienes {0} años.".format (edad_2, nombre_2))

