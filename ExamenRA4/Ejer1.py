def outputFixer(contador, vocal):
    if contador == 0:
        return "La vocal " + vocal + " no aparece ninguna vez"
    elif contador == 1:
        return "La vocal " + vocal + " aparece " + str(contador) + " vez"
    else:
        return "La vocal " + vocal + " aparece " + str(contador) + " veces"

def cuentaVocales(cadena):
    contA = 0
    contE = 0
    contI = 0
    contO = 0
    contU = 0
    for vocal in cadena:
        if vocal == 'a':
            contA += 1
        if vocal == 'e':
            contE += 1
        if vocal == 'i':
            contI += 1
        if vocal == 'o':
            contO += 1
        if vocal == 'u':
            contU += 1

    return outputFixer(contA, "a"), outputFixer(contE, "e"), outputFixer(contI, "i"), outputFixer(contO, "o"), outputFixer(contU, "u")

print(cuentaVocales("me duele el estemocleidomastoideo"))