"""En python es posible acceder a partes específicas de una cadena de carácteres,
también llamadas substrings o subcadenas.

Un substring o subcadena es una sucesión de carácteres dentro de una cadena 
principal (caracteres, palabras, oraciones, símbolos,etc)."""

String = "123456789"
substring = ""

print (f"Cadena principal: {String}")

substring = String [0]
print (f"\nSubcadena con índice en la posición [0] es: {substring}")

substring = String [5]
print (f"\nSubcadena con índice en la posición [5] es: {substring}")

substring = String [-4]
print (f"\nSubcadena con índice en la posición [-4] es: {substring}")

substring = String [0:3]
print (f"\nSubcadena con índices en las posiciones [0:3] es: {substring}")

substring = String [:3]
print (f"\nSubcadena con índices en las posiciones [:3] es: {substring}")

substring = String [5:]
print (f"\nSubcadena con índices en las posiciones [5:] es: {substring}")

substring = String [-4:-1]
print (f"\nSubcadena con índices en las posiciones [-4:-1] es: {substring}")

substring = String [:]
print (f"\nSubcadena con índices en las posiciones [:] es: {substring}")

substring = String [1:6:2]
print (f"\nSubcadena con índices en las posiciones y salto [1:6:2] es: {substring}")

substring = String [::3]
print (f"\nSubcadena con índices en las posiciones y salto [::3] es: {substring}")