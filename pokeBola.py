class Pokemon(object):
	def __init__(self,nombre,poder=10):
		self.nombre = nombre
		self.vida = 100
		self.poder = poder

	def sayName(self):
		print(self.nombre*2)


class Fuego(Pokemon):
	# def __init__(self):
	tipo = 'Fuego'

	def ataquePrincipal(self,objecto):
		objecto.vida -=self.poder
		print(self.sayName()," puto!")
		objecto.checkVida()

	def checkVida(self):
		if self.vida <=0:
			print('Ya vali ·$·@#',self.sayName())
		else:
			print("ahi te voy perro",self.sayName())