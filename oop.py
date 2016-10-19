class Mesa(object):
	def __init__(self,color='blanco',forma='cuadrada',precio=0):
		self.color = color
		self.forma = forma
		self.precio = precio

	def getPrecio(self):
		print('Mi precio es: ',self.precio)

	def getCotizacion(self,cantidad=1):
		total = self.precio*cantidad
		print(total)
		return total