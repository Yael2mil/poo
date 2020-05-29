class banco():
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

class hsbc(banco):
    
    # atributos
    nombre_banco = 'hsbc'
    camaras = 4
    cajas_fuerte = 3
    empleados = 300
    clientes = 300000

    def __init__(self):
        pass
    # métodos
    def apertura_cuenta(self):
        print("Apertura de cuenta")
    def cierre_cuenta(self):
        print('Cierre de cuenta')
hsbc = hsbc()
hsbc.retiro()
print(hsbc.guardias)