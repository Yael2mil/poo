class Estudiante:
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
    def entregaActividad(self):
        print('entrega de actividad')

class Graduado(Estudiante):
    #atributos
    nombre = 'Yael'
    promedio_final = 10
    edad = 24
    titulo = 'licenciatura'
    matricula = 54334131
    #metodos
    def __init__(self):
        pass
    def generarPago(self):
        print("Generador de pago")
    def certificado(self):
        print("Certificado")
    def consulta(self):
        print("consultando calificaciones de la carrera")
    def entregaActividad(self):
        print("No hay actividades por entregar")
yael = Graduado()
yael.consulta()
yael.entregaActividad()
yael.generarPago()
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