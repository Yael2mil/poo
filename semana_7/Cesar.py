import os
ruta = '/home/runner/poo-20/semana_7/Cesar.txt'
class Cesar:
    def __init__(self):
        pass
    
    def cifrar(self, x):
        archivo = open(x, 'w')
        for lineas in archivo():
            linea_cifrada = ''
            for caracter in lineas:
                caracter_cifrado = ord(caracter)
                caracter_cifrado = chr(caracter_cifrado+ 3)
                linea_cifrada = lineas.replace(caracter, caracter_cifrado)
                print(linea_cifrada)
    
    
    def descifrar(self, archivo):
        for lineas in archivo():
            linea_cifrada = ''
            for caracter in lineas:
                caracter_cifrado = ord(caracter)
                caracter_cifrado = chr(caracter_cifrado)
                linea_cifrada = linea_cifrada + caracter_cifrado
    

while True:
    objeto = Cesar()
    nombre_archivo = input('archivo: ')
    try:
        open(nombre_archivo, 'r')
        print('archivo encontrado')
        close(nombre_archivo)

    except:
        print('Archivo no encontrado')
        break
    print('Cifrar 1')
    print('decifrar 2')
    pregunta = int(input('¿Qué realizará? '))
    if pregunta == 1:
        objeto.cifrar(nombre_archivo)
    elif pregunta == 2:
        objeto.descifrar(nombre_archivo)
