class SerieTv:
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

class BreakingBad(SerieTv):
    #atributos
    nombre = 'Breaking bad'
    temporadas = 5
    capitulos = 62
    protagonista = 'walter white'
    genero = 'policial'
    #Metodo 
    def __init__(self):
        pass
    def episodioSiguiente(self):
        print('reproducir episodio siguiente')
    def serieSimilar(self):
        print('series recomendadas')
    def reproducir(self):
        print("Reanudar")
    def pausar(self):
        print("Detener capitulo")

mejor_serie = BreakingBad()
mejor_serie.reproducir()
mejor_serie.pausar()
mejor_serie.episodioSiguiente()
mejor_serie.serieSimilar()
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