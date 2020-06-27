import os
print(os.getcwd())

class Cesar:
    def __init__(self):
        self.archivo = open("Cesar.txt", "r")
    
    def cifrar(self):
        
        for lineas in self.archivo.readlines():
            linea_cifrada = ''
            for caracter in lineas:
                caracter_cifrado = ord(caracter)
                caracter_cifrado = chr(caracter_cifrado)
                linea_cifrada = linea_cifrada + caracter_cifrado
    def decifrar(self):
        for lineas in self.archivo.readlines():
            linea_cifrada = ''
            for caracter in lineas:
                caracter_cifrado = ord(caracter)
                caracter_cifrado = chr(caracter_cifrado)
                linea_cifrada = linea_cifrada + caracter_cifrado
    





objeto = Cesar()
objeto.cifrar()