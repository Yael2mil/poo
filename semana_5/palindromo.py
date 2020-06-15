class Palindromo: #Definimos la clase
	def __init__(self): #definimos el constructor
		pass
	def comprobador(self, x): #Definimos el metodo que va a analizar si el texto es palindromo
		replacements = (   #listas para reconocer vocales acentuadas
			("á", "a"),
			("é", "e"),
			("í", "i"),
			("ó", "o"),
			("ú", "u"),
		)
		for a, b in replacements: #para utilizar las listas utilizamos las comas, que representan cada letra, una acentuada la otra no
			x = x.replace(a, b).replace(a.upper(), b.upper()) #reemplaza las vocales con acento
		x = x.replace(' ','') #Elimina los espacios
		cadena_inversa = ''.join(reversed(x)) #invierte la cadena
		if x == cadena_inversa: #comprueba si es un palindromo
			print('Es un palindromo') #imprime el resultado
		else:  #Si la palabra no es palindromo
			print('No es un palindromo')
	def contador(self, x): #Metodo para contar vocales y espacios
		no_vocales = 0 #creamos variable para poder usar "+="
		no_espacios = 0 
		vocales = 'aeiouáéíóúAEIOUÁÉÍÓÚüÜ'#constante con las vocales
		for caracter in x: #lee cada caracter en la cadena
			if caracter in vocales: #identifica si es una vocal
				no_vocales += 1 #suma una vocal
			if caracter == ' ': #identifica si es un espacio
				no_espacios += 1 #suma un espacio
		print('Hay {} vocales y  {} espacios.'.format(self.no_vocales, self.no_espacios)) #imprime el resultado
while True: #Para usar el codigo cuantas veces se quiera
	texto = input('Ingrese texto a analizar: ') #Entrada de texto
	hola = Palindromo() #Crea un objeto
	hola.comprobador(texto) #llama al metodo para analizar
	hola.contador(texto) #llama al metodo para contar
	otra = input("¿Desea analizar otra cadena s/n?: ") #entrada que influye en el bucle while
	if not (otra == "s" or otra == "S"): #condicion para analizar la entrada
		break #rompe el bucle while