class estudiante():
    #atributos
    promedio = 9.8
    edad_minima = 17
    entidad = 'tulancingo' 
    carrera = "TIC's"
    nivel = 'Universidad'
    # metodos
    def __init__(self):
        pass
    def consulta(self):
        print('consulta')
    def entrega_actividad(self):
        print('entrega de actividad')

class graduado():
    #atributos
    nombre = 'Yael'
    promedio_final = 10
    edad = 24
    titulo = 'licenciatura'
    matricula = 54334131
    #metodos
    def __init__(self):
        pass
    def generar_pago(self):
        print("Generador de pago")
    def certificado(self):
        print("Certificado")
