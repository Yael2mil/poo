class serie_tv():
    #atributos
    plataforma = 'netflix'
    resolucion = '3840 x 2160'
    generos = ['drama', 'suspenso', 'romance']
    productora = 'sony pictures'
    idioma = 'español'
    #metodo
    def __init__(self):
        pass
    def reproducir(self):
        print('reproducir')
    def pausar(self):
        print('pausar')

class breaking_bad(serie_tv):
    #atributos
    nombre = 'Breaking bad'
    temporadas = 5
    capitulos = 62
    protagonista = 'walter white'
    genero = 'policial'
    #Metodo 
    def __init__(self):
        pass
    def episodio_siguiente(self):
        print('reproducir episodio siguiente')
    def serie_similar(self):
        print('series recomendadas')

mejor_serie = breaking_bad()
mejor_serie.reproducir()
mejor_serie.pausar()
mejor_serie.episodio_siguiente()
mejor_serie.serie_similar()
print(mejor_serie.plataforma)
print(mejor_serie.resolucion)
print(mejor_serie.generos)
print(mejor_serie.productora)
print(mejor_serie.idioma)
print(mejor_serie.nombre)
print(mejor_serie.temporadas)
print(mejor_serie.capitulos)
print(mejor_serie.protagonista)
print(mejor_serie.genero)