print ("Sistema para calcular el promedio de un alumno.")

nombre = input ("Para comenzar escribe tu nombre: ")
matematicas = int ( input (nombre + " ¿Cuál es tu calificación en matemáticas?: "))
quimica = int ( input (nombre + " ¿Cuál es tu calificación en química?: "))
biologia = int ( input (nombre +" ¿Cuál es tu calificación en biología?: "))

promedio = (matematicas + quimica + biologia) // 3

if promedio >= 6:
	print ('Felicidades ' + nombre + ' "aprobaste" con un promedio de:',promedio)
else:
	print ( nombre + ' Lamentablemente tu promedio no es suficiente, has reprobado con un promedio de:',promedio)

print ("Eso es todo")

"""Las sentencias condicionales simples son las que no ejecutan nada si la condición
no se cumple, sin embargo, las que si ejecutan una instrucción si no se cumple la 
condición son sentencias condicionales compuestas"""