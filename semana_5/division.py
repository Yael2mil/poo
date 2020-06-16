dividendo = float(input('Dividendo: '))
divisor = float(input('Divisor: '))
cociente = 0

division = 0
while division < dividendo:
    cociente += 1
    division = divisor * cociente
residuo = division - dividendo
if residuo > 0:
    cociente -= 1
    x = 0
    while residuo < divisor:
        x +=1
        y = (float(residuo) * 0.1)*x
        residuo = residuo * 10
        while cociente*divisor < dividendo:
            cociente+= y 
print(cociente)
