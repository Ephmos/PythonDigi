def calculaPosicion(n, datos):
    x = 0
    posiciones = []
    while x < len(datos):
        if datos[x] == n:
            posiciones.append(x)
        x+=1

    if len(posiciones) == 0:
        return -1
    else:
        return posiciones

valores = [1000, 500, 2, 5, 1, 5, 2, 4, 5]
print(calculaPosicion(5, valores))

valores2 = [1,2,3,4]
print(calculaPosicion(5, valores2))

valores3 = [1,2,3,4,5]
print(calculaPosicion(5, valores3))


