class Banco:
    # atributos
    guardias = 2
    cajeros = 12
    ventanillas = 8
    piso = 'blanco'
    puertas = 3

    def __init__(self):
        pass
    # métodos
    def deposito(self):
        print("deposito")
    def retiro(self):
        print("retiro")

class Hsbc(Banco):
    
    # atributos
    nombre_banco = 'hsbc'
    camaras = 4
    cajas_fuerte = 3
    empleados = 300
    clientes = 300000

    def __init__(self):
        pass
    # métodos
    def aperturaCuenta(self):
        print("Apertura de cuenta")
    def cierreCuenta(self):
        print('Cierre de cuenta')
    def deposito(self):
        print('deposito desde practicaja')
    def retiro(self):
        print('retiro desde cajero')
hsbc = Hsbc()
hsbc.deposito()
hsbc.retiro()
hsbc.aperturaCuenta()
hsbc.cierreCuenta()

print(hsbc.guardias)
print(hsbc.cajeros)
print(hsbc.ventanillas)
print(hsbc.piso)
print(hsbc.puertas)
print(hsbc.nombre_banco)
print(hsbc.camaras)
print(hsbc.cajas_fuerte)
print(hsbc.empleados)
print(hsbc.clientes)