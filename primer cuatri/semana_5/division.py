dividendo = float(input('Dividendo: '))
divisor = float(input('Divisor: '))
cociente = 0

division = 0
while division < dividendo:
    cociente += 1
    division = divisor * cociente
residuo = division - dividendo

while residuo > 0:
    cociente -= 1
    x = 0
    terminar1= residuo < divisor
    y = 1
    while terminar1:
        x +=1
        y = y * 0.1
        residuo = residuo * 10
        residuo = residuo - cociente*divisor
        terminar = True
        while terminar:
            cociente+= y
            if cociente*divisor > dividendo:
                cociente -=y
                terminar= False
        if x == 10:
            terminar1 = False
            residuo = 0
        

print(cociente)
