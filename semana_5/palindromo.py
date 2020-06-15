class Palindromo:
	"""docstring for Palindromo"""
	def __init__(self):
		self.no_vocales = 0
		self.no_espacios = 0
	def comprobador(self, x):
		replacements = (
			("á", "a"),
			("é", "e"),
			("í", "i"),
			("ó", "o"),
			("ú", "u"),
		)
		texto = x
		for a, b in replacements:
			texto = texto.replace(a, b).replace(a.upper(), b.upper())
		texto = texto.replace(' ','')
		print(texto)
		cadena_inversa = ''.join(reversed(texto))
		print(cadena_inversa)
		if texto == cadena_inversa:
			print('Es un palindromo')
		else:
			print('No es un palindromo')
	def contador(self, x):
		vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚüÜ'
		for caracter in x:
			if caracter in vocales:
				self.no_vocales += 1
			if caracter == ' ':
				self.no_espacios += 1
		print('Hay {} vocales y  {} espacios.'.format(self.no_vocales, self.no_espacios))
while True:
	texto = input('Ingrese texto a analizar: ')
	hola = Palindromo()
	hola.comprobador(texto)
	hola.contador(texto)
	otra = input("¿Desea analizar otra cadena s/n?: ") #entrada que influye en el bucle while
	if not (otra == "s" or otra == "S"): #condicion para analizar la entrada
		break #rompe el bucle while