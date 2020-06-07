class Futbolista:
    #atributos
    uniforme = 'jersey'
    calzado = 'tacos de futbol'
    deporte = 'futbol'
    entrenamiento = 'entrenamiento diario'
    estadio = 'estadio local'
    #metodos
    def __init__(self):
        pass
    def tirar(self):
        print('tirar')
    def entrada(self):
        print('entrada')
class Barcelona(Futbolista):
    equipo = 'Barcelona'
    altura = 1.90
    velocidad = 36
    posicion = 'atacante'
    cabello = 'lasio'
    #metodos 
    def __init__(self):
        pass
    def regate(self):
        print('hacer un regate')
    def correr(self):
        print('correr')
    def tirar(self):
        print("tiro a puerta")
    def entrada(self):
        print("entrada agresiva")
messi = Barcelona()
messi.tirar()
messi.entrada()
messi.regate()
messi.correr()
print(messi.uniforme)
print(messi.calzado)
print(messi.deporte)
print(messi.entrenamiento)
print(messi.estadio)
print(messi.equipo)
print(messi.altura)
print(messi.velocidad)
print(messi.posicion)
print(messi.cabello)