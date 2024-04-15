#El comando input se utiliza para solicitar datos desde el teclado
#Num_int = número entero
#int transforma el dato en un dato de tipo entero 
palabra = input ("Introduce una palabra: ")
num_int = int (input ("Introduce un número entero: "))
num_float = float (input ("Introduce un número flotante: "))
num_complex = complex (input ("Introduce un número complejo: "))


print ("String: ", palabra)
print ("Número entero: ", num_int)
print ("Número flotante: ", num_float)
print ("Número complejo: ", num_complex)

Nombre = input ("¿Como te llamas?: ")
print ("Hola " + Nombre + ", vamos a hacer una suma.")

numero_uno = float (input ("Por favor introduce el primer valor: "))
numero_dos = float (input ("Ahora por favor introduce el segundo valor: "))

print (Nombre, "El resultado de la suma es: ", numero_uno + numero_dos)

