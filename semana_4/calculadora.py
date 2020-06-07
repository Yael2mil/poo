class Calculadora:
    #atributos
    operaciones = ['suma', 'resta']
    color = 'negro'
    entrada = 'botones'
    datos_ingresar = 2
    caracteres = 12
    #metodos
    def __init__(self):
        pass
    def sumar(self):
        print('sumar')
    def restar(self):
        print('restar')
class CalculadoraCientifica(Calculadora):
    #atributos
    tipo = 'cientifica'
    operaciones_extra = ['raiz cuadrada']
    funciones_trigonometricas = ['coseno', 'seno','tangente']
    botones = 68
    panel = '35 caracteres'
    #metodos
    def __init__(self):
        pass
    def raizCuadrada(self):
        print('raiz cuadrada')
    def potencia(self):
        print('potencia')
    def sumar(self):
        print("sumar n cantidad de elementos")
    def restar(self):
        print("restar n cantidad de datos")
casio = CalculadoraCientifica()
casio.sumar()
casio.restar()
casio.raizCuadrada()
casio.potencia()
print(casio.operaciones)
print(casio.color)
print(casio.entrada)
print(casio.datos_ingresar)
print(casio.caracteres)
print(casio.tipo)
print(casio.operaciones_extra)
print(casio.funciones_trigonometricas)
print(casio.botones)
print(casio.panel)