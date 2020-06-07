class Vacaciones:
    #atributos
    duracion = '1 semana'
    motivo = 'semana santa'
    fin = 'lunes 13 de abril'
    sitio_turistico = 'cancun'
    presupuesto = 15000
    #metodos
    def __init__(self):
        pass
    def alquilarHabitacion(self):
        print('alquilar una habitacion')
    def cotizarPrecios(self):
        print('cotizaje de precios')
class Hospedaje(Vacaciones):
    #atributos
    hotel = 'Hilton'
    costo_habitacion = 600
    menu = ['desayunos', 'postres', 'aperitivos']
    capacidad_piscina = '5000l'
    actividad_principal = 'dia en la playa'
    #metodos
    def __init__(self):
        pass
    def pedidoComida(self):
        print('pedido de comida')
    def agendarActividad(self):
        print('agendar una actividad')
    def alquilarHabitacion(self):
        print("la habitacion a sido alquilada")
    def cotizarPrecios(self):
        print("cotizar habitaciones")
familia_romeo = Hospedaje()
familia_romeo.alquilarHabitacion()
familia_romeo.cotizarPrecios()
familia_romeo.pedidoComida()
familia_romeo.agendarActividad()
print(familia_romeo.duracion)
print(familia_romeo.motivo)
print(familia_romeo.fin)
print(familia_romeo.sitio_turistico)
print(familia_romeo.presupuesto)
print(familia_romeo.hotel)
print(familia_romeo.costo_habitacion)
print(familia_romeo.menu)
print(familia_romeo.capacidad_piscina)
print(familia_romeo.actividad_principal)