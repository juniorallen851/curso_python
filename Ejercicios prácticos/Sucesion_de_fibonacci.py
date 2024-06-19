variable = 0
variable_2 = 1
print (variable, variable_2, end=" ")
while not variable_2 == 1597:
	variable += variable_2
	variable_2 += variable
	print (variable, variable_2, end = " ")