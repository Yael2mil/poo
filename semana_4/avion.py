class Avion:
    #atributos
    alas = 2
    cabina = 1
    pilotos = 2
    alerones = 2
    timon = 1
    #metodos
    def __init__(self):
        pass
    def ascender(self):
        print('Ascender')
    def descender(self):
        print('Descender')

class VueloComercial(Avion):
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
    def ascender(self):
        print("ascendiendo a 6000 pies")
    def descender(self):
        print("descendiendo altitud")
    
aeromexico = VueloComercial()
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
print(aeromexico.aerolinea)
print(aeromexico.aeromosas)
print(aeromexico.capacidad_tanque)
print(aeromexico.capacidad_peso)