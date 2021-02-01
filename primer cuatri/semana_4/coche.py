class Coche:
    #atributos
    llantas = 'pirelli'
    combustible = 'gasolina'
    pasajeros = 5
    cilindros_motor = 4
    luces = 'faros'
    #metodos
    def __init__(self):
        pass
    def acelerar(self):
        print('acelerar')
    def frenar(self):
        print('frenar')
class Nissan(Coche):

    #atributos
    marca = 'nissan'
    linea = 'aveo'
    color = 'blanco'
    velocidad_maxima = '250 km/hr'
    capacidad_combustible = '100 litros'
    #metodos
    def __init__(self):
        pass
    def abrirPuerta(self):
        print('abrir puerta')
    def encender(self):
        print('encender')
    def acelerar(self):
        print("acelerando vehiculo")
    def frenar(self):
        print("Frenando vehiculo")
aveo = Nissan()
aveo.acelerar()
aveo.frenar()
aveo.abrirPuerta()
aveo.encender()
print(aveo.llantas)
print(aveo.combustible)
print(aveo.pasajeros)
print(aveo.cilindros_motor)
print(aveo.luces)
print(aveo.marca)
print(aveo.linea)
print(aveo.color)
print(aveo.velocidad_maxima)
print(aveo.capacidad_combustible)