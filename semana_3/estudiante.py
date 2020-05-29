class estudiante():
    #atributos
    promedio = 9.8
    instituto = 'Universidad tecnologica de Tulancingo'
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

class graduado(estudiante):
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
yael = graduado()
yael.consulta()
yael.entrega_actividad()
yael.generar_pago()
yael.certificado()
print(yael.promedio)
print(yael.instituto)
print(yael.entidad)
print(yael.carrera)
print(yael.nivel)
print(yael.nombre)
print(yael.promedio_final)
print(yael.edad)
print(yael.titulo)
print(yael.matricula)