class classroom():
    #atributos
    color = 'verde'
    clases = 6
    alumnos = 600
    profesores = 8
    actividades_pendientes = 10
    #metodos
    def __init__(self):
        pass
    def ingresar_clase(self):
        print('ingresar a una nueva clase')
    def subir_actividad(self):
        print('subir una actividad')
class poo(classroom):
    #atributos
    color_clase = 'rojo'
    actividades = 6
    profesor = 'Juan'
    alumno = 'Yael'
    materia = 'programacion orienta a objetos'
    #metodos
    def __init__(self):
        pass
    def consulta_calificaciones(self):
        print('consulta de calificaciones')
    def consultar_material(self):
        print('consultar material')
yael = poo()
yael.ingresar_clase()
yael.subir_actividad()
yael.consulta_calificaciones()
yael.consultar_material()
print(yael.color)
print(yael.clases)
print(yael.alumnos)
print(yael.profesores)
print(yael.actividades_pendientes)
print(yael.color_clase)
print(yael.actividades)
print(yael.profesor)
print(yael.alumno)
print(yael.materia)