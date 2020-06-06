class LecturaString: #definimos la clase
    def __init__(self):   #definimos el constructor
        self.texto = input("ingrese el texto a analizar: ") #entrada para ingresar el texto cada que se cree un objeto
    
    def lectorCaracter(self): #definimos la funcion para analizar los caracteres
        for caracter in self.texto: #para analizar cada caracter de la cadena
            print('"{}"'.format(caracter)) #imprime cada caracter para saber de cual se esta hablando
            if caracter.isalpha():  #analiza si el caracter es una letra
                print('Es una letra') #imprime el resultado
            elif caracter.isnumeric(): #analiza si el caracter es un numero
                print('Es un numero') #imprime el resultado
            else:  #al no estar dentro de las anteriores damos por hecho que el caracter será un simbolo
                print('Es un simbolo') #imprime el resultado
    
    def longuitudes(self): #funcion para analizar las longuitudes
        longuitud_espacios = len(self.texto) #cuenta los caracteres incluyendo espacios
        self.eliminador_espacios = self.texto.replace(" ","") #elimina los espacios y guarda el resultado en una variable
        longuitud_sin_espacios = len(self.eliminador_espacios) #cuenta los caracteres de la variable anterior
        print("Hay {} caracteres".format(longuitud_espacios)) #imprime el numero de caracteres con espacios
        print("Hay {} caracteres, sin contar espacios".format(longuitud_sin_espacios)) #imprime el numero de caracteres sin espacios

diccionario_lecturas = {} #creamos un diccionario para guardar las lecturas en caso de ser necesario
no_lecturas = 0 #un control para saber cuantas lecturas hay

while True:
    no_lecturas += 1  #añadimos una lectura nueva
    lectura = LecturaString() #declaramos un objeto en la clase
    lectura.lectorCaracter()    #llamamos al metodo de lector
    lectura.longuitudes()   #llamamos al metodo de longuitudes
    diccionario_lecturas['Lectura {}'.format(no_lecturas)] = lectura
    otra = input("¿Desea analizar otra cadena s/n?: ") #entrada que influye en el bucle while
    if not (otra == "s" or otra == "S"): #condicion para analizar la entrada
        break #rompe el bucle while