class vacaciones():
    #atributos
    duracion = '1 semana'
    motivo = 'semana santa'
    fin = 'lunes 13 de abril'
    sitio_turistico = 'cancun'
    presupuesto = 15000
    #metodos
    def __init__(self):
        pass
    def alquilar_habitacion(self):
        print('alquilar una habitacion')
    def cotizar_precios(self):
        print('cotizaje de precios')
class hospedaje(vacaciones):
    #atributos
    hotel = 'Hilton'
    costo_habitacion = 600
    menu = ['desayunos', 'postres', 'aperitivos']
    capacidad_piscina = '5000l'
    actividad_principal = 'dia en la playa'
    #metodos
    def __init__(self):
        pass
    def pedido_comida(self):
        print('pedido de comida')
    def agendar_actividad(self):
        print('agendar una actividad')

familia_romeo = hospedaje()
familia_romeo.alquilar_habitacion()
familia_romeo.cotizar_precios()
familia_romeo.pedido_comida()
familia_romeo.cotizar_precios()
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