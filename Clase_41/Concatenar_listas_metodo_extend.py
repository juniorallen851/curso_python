invitados = ["Carolina", "Carmen", "Robert"]
amigos = ["Alex", "Adriana"]
print ()
print (f"Lista de invitados: {invitados}")
print (f"Lista de amigos: {amigos}")
invitados.extend(amigos)
print (f"\nLista de invitados: {invitados}")
print ()

numeros = [10, 20]
print (f"Lista de números: {numeros}")
numeros.extend(range (30, 100, 10))
print (f"Lista de números: {numeros}")