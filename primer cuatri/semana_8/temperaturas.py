class Temperaturas:
    def __init__(self):
        pass
    
    def convertir(self, celsius):
        fahrenheit = (celsius * 9 / 5) + 32
        print('equivale a {} grados fahrenheit.'.format(fahrenheit))
        archivo = open('temperaturas.txt', 'a')
        archivo.write('{}, {}\n'.format(celsius, fahrenheit) )
        archivo.close()

    def promedio(self):
        archivo = open('temperaturas.txt', 'r')
        n_temperaturas = 0
        suma_celsius = 0
        suma_fahrenheit = 0
        for linea in archivo.readlines():
            temp = linea.replace("\n", "")
            temp = temp.split(', ')
            n_temperaturas += 1
            suma_celsius += float(temp[0])
            suma_fahrenheit += float(temp[1])
        
        promedio_celsius = suma_celsius / n_temperaturas
        print('el promedio es de {}° celsius.'.format(promedio_celsius))
        promedio_fahrenheit = suma_fahrenheit / n_temperaturas
        print('y de {}° fahrenheit.'.format(promedio_fahrenheit))
        archivo.close()
        


while True:
    objeto = Temperaturas()
    temperatura = int(input('Ingrese la temperatura en grados Celsius: '))
    objeto.convertir(temperatura)
    otra = input("¿Desea introducir otra temperatura s/n?: ") #entrada que influye en el bucle while
    if not (otra == "s" or otra == "S"): #condicion para analizar la entrada
        objeto.promedio()
        remove('temperaturas.txt')
        break #rompe el bucle while