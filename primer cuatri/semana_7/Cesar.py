from os import remove #para eliminar archivos
class Cesar:#definimos la clase 
    def __init__(self): #constructor
        pass
    
    def cifrar(self): #metodo
        archivo = open(nombre_archivo, 'r')#abre el archivo en modo lectura
        cifrado = '' #variable que guardara el texto cifrado
        for linea in archivo.readlines(): #separa el archivo por lineas
            linea_cifrada= '' #guarda los renglones cifrados
            for caracter in linea: #separa cada caracter de las lineas
                caracter_cifrado = ord(caracter) #transforma a ascii
                caracter_cifrado = chr(caracter_cifrado + 3) #transforma a caracter cifrado
                linea_cifrada = linea_cifrada + caracter_cifrado
            cifrado = cifrado + linea_cifrada + '\n'
        archivo.close()
        remove(nombre_archivo)
        archivo = open (nombre_archivo, "w")
        archivo.write(cifrado)
        
    
    
    def descifrar(self):
        archivo = open(nombre_archivo, 'r')
        cifrado = ''
        for linea in archivo.readlines():
            linea_cifrada= ''
            for caracter in linea:
                caracter_cifrado = ord(caracter)
                caracter_cifrado = chr(caracter_cifrado - 3)
                linea_cifrada = linea_cifrada + caracter_cifrado
            cifrado = cifrado + linea_cifrada + '\n'
        archivo.close()
        remove(nombre_archivo)
        archivo = open (nombre_archivo, "w")
        archivo.write(cifrado)
    

while True:
    objeto = Cesar()
    nombre_archivo= input('Ingresa el nombre del archivo: ')
    print('Cifrar 1')
    print('decifrar 2')
    pregunta = int(input('¿Qué realizará? '))
    if pregunta == 1:
        objeto.cifrar()
    elif pregunta == 2:
        objeto.descifrar()
    else: 
        print('error')
    otra = input("¿Desea analizar otra cadena s/n?: ") #entrada que influye en el bucle while
    if not (otra == "s" or otra == "S"): #condicion para analizar la entrada
        break #rompe el bucle while
