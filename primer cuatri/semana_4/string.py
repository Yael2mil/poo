while True:    #creamos el bucle while, para que el codigo se repita las veces necesarias
    texto = input('introduzca la cadena a analizar: ')   #interactua con el programa para ingresar el texto a analizar
    for caracter in texto: #el bucle for se encargara de leer el texto caracter por caracter
        print('"{}"'.format(caracter)) #imprime cada caracter para saber de cual se esta hablando
        if caracter.isalpha():  #analiza si el caracter es una letra
            print('Es una letra') #imprime el resultado
        elif caracter.isnumeric(): #analiza si el caracter es un numero
            print('Es un numero') #imprime el resultado
        else:  #al no estar dentro de las anteriores damos por hecho que el caracter será un simbolo
            print('Es un simbolo') #imprime el resultado
    print("no. de caracteres: ",len(texto)) #imprime la longuitud de la cadena
    sinespacios = texto.replace(" ", "") #elimina los espacios y los guarda en una nueva variable
    print("no. de caracteres sin espacios: ",len(sinespacios)) #imprime la longuitud de la cadena sin espacios
    otra = input("¿Desea analizar otra cadena s/n?: ") #entrada que influye en el bucle while
    if not (otra == "s" or otra == "S"): #condicion para analizar la entrada
        break #rompe el bucle while
class LecturaString:
    def __init__(self):
        self.texto = input("ingrese el texto")