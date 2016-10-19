lista = list(map(int,input("dame una lista de numeros separados por espacio: ").split("-")))


def mayor(lista):
	aux = 0
	for num in lista:
		if num>aux:
			aux = num
	return aux


def menor(lista):
	aux = lista[0]
	for num in lista:
		if num<aux:
			aux = num
	return aux

def suma(lista):
	aux = 0
	for num in lista:
		aux += num
	return aux

print("esta es la lista: ",lista)
print("El menor: ",menor(lista))
print("El mayor: ",mayor(lista))
print("La suma: ",suma(lista))


