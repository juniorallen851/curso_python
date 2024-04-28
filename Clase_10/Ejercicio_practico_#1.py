print ("===========================")
print ("Sistema Vacacional de RAPPI")
print ("===========================\n")

nombre_del_empleado = input ("Por favor introduce el nombre del empleado: ")
Clave_del_departamento = int (input ("Introduce la clave del clave del departamento: "))
antigüedad_del_empleado = int (input ("Introduce los años laborados del empleado: "))

if Clave_del_departamento == 1:

	if antigüedad_del_empleado < 1:
		print ("El empleado" ,nombre_del_empleado, "aún no tiene derecho a vacaciones.")

	elif antigüedad_del_empleado >= 1 and antigüedad_del_empleado <= 2:
		print ("El empleado", nombre_del_empleado, "tiene derecho a 6 dias de vacaciones.")

	elif antigüedad_del_empleado >= 2 and antigüedad_del_empleado <= 6:
	    print ("El empleado", nombre_del_empleado, "tiene derecho a 14 dias de vacaciones.")

	elif antigüedad_del_empleado >= 7:
		print ("El empleado", nombre_del_empleado, "tiene derecho a 20 dias de vacaciones.")

	else:
		("El empleado" ,nombre_del_empleado, "aún no tiene derecho a vacaciones.")



elif Clave_del_departamento == 2:

	if antigüedad_del_empleado < 1:
		print ("El empleado" ,nombre_del_empleado, "aún no tiene derecho a vacaciones.")

	elif antigüedad_del_empleado >= 1 and antigüedad_del_empleado <= 2:
		print ("El empleado", nombre_del_empleado, "tiene derecho a 7 dias de vacaciones.")

	elif antigüedad_del_empleado >= 2 and antigüedad_del_empleado <= 6:
	    print ("El empleado", nombre_del_empleado, "tiene derecho a 15 dias de vacaciones.")

	elif antigüedad_del_empleado >= 7:
		print ("El empleado", nombre_del_empleado, "tiene derecho a 22 dias de vacaciones.")

	else:
		("El empleado" ,nombre_del_empleado, "aún no tiene derecho a vacaciones.")

elif Clave_del_departamento == 3:

	if antigüedad_del_empleado < 1:
		print ("El empleado" ,nombre_del_empleado, "aún no tiene derecho a vacaciones.")

	elif antigüedad_del_empleado >= 1 and antigüedad_del_empleado <= 2:
		print ("El empleado", nombre_del_empleado, "tiene derecho a 10 dias de vacaciones.")

	elif antigüedad_del_empleado >= 2 and antigüedad_del_empleado <= 6:
	    print ("El empleado", nombre_del_empleado, "tiene derecho a 20 dias de vacaciones.")

	elif antigüedad_del_empleado >= 7:
		print ("El empleado", nombre_del_empleado, "tiene derecho a 30 dias de vacaciones.")

	else:
		("El empleado" ,nombre_del_empleado, "aún no tiene derecho a vacaciones.")	

else:
	print ("La clave del departamento no existe, vuelve a intentarlo.")

