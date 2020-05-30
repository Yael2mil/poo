class avion():
    #atributos
    alas = 2
    cabina = 1
    pilotos = 2
    alerones = 2
    timon = 1
    #metodos
    def __init__(self):
        pass
    def ascencer(self):
        print('Ascender')
    def descender(self):
        print('Descender')

class comercial(avion):
    #atributos
    pasajeros = 300
    aerolinea = 'aeromexico'
    aeromosas = 5
    capacidad_tanque = "200000 litros"
    capacidad_peso = "250 toneladas"
    #metodos
    def __init__(self):
        pass
    def despegue(self):
        print('despegue')
    def aterrizaje(self):
        print('aterrizaje')

aeromexico = comercial()
aeromexico.ascender()
aeromexico.descender()
aeromexico.despegue()
aeromexico.aterrizaje()
print(aeromexico.alas)
print(aeromexico.cabina)
print(aeromexico.pilotos)
print(aeromexico.alerones)
print(aeromexico.timon)
print(aeromexico.pasajeros)
print(aeromexico.aerolina)
print(aeromexico.aeromosas)
print(aeromexico.capacidad_tanque)
print(aeromexico.capacidad_peso)
