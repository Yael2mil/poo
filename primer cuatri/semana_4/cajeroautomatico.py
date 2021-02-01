class CajeroAutomatico:
    #atributos
    efectivo = 500000
    panel = 'panel touch'
    sucursal = 'tulancingo'
    banco = 'santander'
    retiro_maximo = 9600
    #metodos
    def __init__(self):
        pass
    def retiro(self):
        print('retiro')
    def leerTarjeta(self):
        print('leer tarjeta')
class PractiCaja(CajeroAutomatico):
    #atributos
    color = 'gris'
    botones = 6 
    pantalla = 26.6
    tiempo_espera = '2 minutos'
    cliente = 'Yael'
    #metodos
    def __init__(self):
        pass
    def deposito(self):
        print('deposito')
    def transaccion(self):
        print('transaccion')
    def retiro(self):
        print("retiro desde practi-caja")
    def leerTarjeta(self):
        print("Aguarde un momento leyendo su tarjeta")
cajero1 = PractiCaja()
cajero1.retiro()
cajero1.leerTarjeta()
cajero1.deposito()
cajero1.transaccion()
print(cajero1.efectivo)
print(cajero1.panel)
print(cajero1.sucursal)
print(cajero1.banco)
print(cajero1.retiro_maximo)
print(cajero1.color)
print(cajero1.botones)
print(cajero1.tiempo_espera)
print(cajero1.cliente)
print(cajero1.pantalla)