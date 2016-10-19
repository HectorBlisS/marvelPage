lista = [2,5,1,4,9,7,8,6]
print("la lista: ",lista)
for i in range(1,len(lista)):
	j = i
	while j > 0 and lista[j] < lista[j-1]:
		lista[j],lista[j-1] = lista[j-1],lista[j]
		j-=1
	print(lista)

