class calculadora():
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
class cientifica(calculadora):
    #atributos
    tipo = 'cientifica'
    operaciones_extra = ['raiz cuadrada']
    funciones_trigonometricas = ['coseno', 'seno','tangente']
    botones = 68
    panel = '35 caracteres'
    #metodos
    def __init__(self):
        pass
    def raiz_cuadrada(self):
        print('raiz cuadrada')
    def potencia(self):
        print('potencia')
casio = cientifica()
casio.sumar()
casio.restar()
casio.raiz_cuadrada()
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