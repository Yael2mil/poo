class Classroom:
    #atributos
    color = 'verde'
    clases = 6
    alumnos = 600
    profesores = 8
    actividades_pendientes = 10
    #metodos
    def __init__(self):
        pass
    def ingresarClase(self):
        print('ingresar a una nueva clase')
    def subirActividad(self):
        print('subir una actividad')
class Poo(Classroom):
    #atributos
    color_clase = 'rojo'
    actividades = 6
    profesor = 'Juan'
    alumno = 'Yael'
    materia = 'programacion orienta a objetos'
    #metodos
    def __init__(self):
        pass
    def consultaCalificaciones(self):
        print('consulta de calificaciones')
    def consultarMaterial(self):
        print('consultar material')
    def ingresarClase(self):
        print("bienvenido a la clase")
    def subirActividad(self):
        print("Subiendo actividad a Poo")
yael = Poo()
yael.ingresarClase()
yael.subirActividad()
yael.consultaCalificaciones()
yael.consultarMaterial()
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