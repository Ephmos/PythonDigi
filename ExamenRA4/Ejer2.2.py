def calculaPosicionAñade(n, datos):
    x = 0
    posiciones = []
    while x < len(datos):
        if datos[x] == n:
            posiciones.append(x)
        x+=1

    if len(posiciones) == 0:
        try:
            datos.insert(n-1, n)
        except IndexError:
            datos.append(n)

valores = [5, 5, 5, 5]
calculaPosicionAñade(4, valores)
print(valores)