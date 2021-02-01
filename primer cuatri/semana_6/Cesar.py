'class CodigoCesar:
    def __init__(self):
        self.cadena = input('ingrese el texto a analizar: ')
    def codificar(self):
        texto_Codificado = ''
        for caracter in self.cadena:
            codificado = ord(caracter)
            codificado = chr(codificado+3)
            texto_Codificado = texto_Codificado + caracter.replace(caracter, codificado)
        print(texto_Codificado)
    def decodificar(self):
        texto_Decodificado = ''
        for caracter in self.cadena:
            decodificado = ord(caracter)
            decodificado = chr(decodificado-3)
            texto_Decodificado = texto_Decodificado + caracter.replace(caracter, decodificado)
        print(texto_Decodificado)
        
while True:
    objeto = CodigoCesar()
    print('Codificar: 1.')
    print('Decodificar: 2.')
    respuesta = int(input('Que quiere hacer con el texto? '))
    if respuesta == 1:
        objeto.codificar()
    elif respuesta == 2:
        objeto.decodificar()
    else:
        print('no valido.')
    otra = input("¿Desea analizar otra cadena s/n?: ") #entrada que influye en el bucle while
    if not (otra == "s" or otra == "S"): #condicion para analizar la entrada
        break #rompe el bucle while