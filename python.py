import random

# lista = ["piedra","papel","tijera"]
# robot = random.choice(lista)
robot = random.randint(1,3)
user = 1

while user < 4:
	print("1.-Piedra\n 2.-Papel\n 3.-Tijera")
	user = int(input("Escoje una opción entre piedra, papel o tijera: "))
	print("Tu opcion: ",user)
	print("Mi opcion: ",robot)
	if robot == user:
		print('Esto es un empate')
	elif robot == 1 and user == 2:
		print("Tu ganas")
	elif robot == 2 and user == 3:
		print("Tu ganas")
	elif robot == 3 and user == 1:
		print("Tu ganas")
	elif robot == 1 and user == 3:
		print("Tu pierdes")
	elif robot == 2 and user == 1:
		print("Tu pierdes")
	elif robot == 3 and user == 2:
		print("Tu pierdes")
print("Gracias por jugar t(O_ot)")


