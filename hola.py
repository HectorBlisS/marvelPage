def saluda():
	""" Hola esta es la ayuda: esta funcion imprime un saludo """
	print("Hola FixterGeeks")
#aqui me despido
def despidete():
	""" se despide """
	print("Adios mijo")

def pide_el_nombre():
	"""
	esta funcion le pide al usuario su nombre
	 y la guarda en un string llamado nombre
	 """
	nombre = input("Hola User dime tu nombre: ")
	print("Hola "+nombre)

def main():
	saluda()
	pide_el_nombre()
	despidete()

# main()