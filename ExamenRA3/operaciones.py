# 1
from math import isnan


def info_argumentos(*args):
    argCounter = 0
    for arg in args:
        print(arg)
        argCounter +=1
    print("El total de argumentos es", argCounter)

def divisibles3(*args: int):
    for arg in args:
        if arg % 3 == 0:
            print(arg)

def histograma(*args: int):
    for arg in args:
        print("*" * arg)
# 2
def coste_envio(peso: int = 0, urgente: bool = False):
    base = 5
    if urgente:
        precioB = base + (peso * 2)
        precioT = precioB + (precioB * 0.3)
        print("El precio de envío calculado para este paquete es", precioT)
    else:
        precioB = base + (peso * 2)
        print("El precio de envío calculado para este paquetes es", precioB)

# 3
def convertir_segundos(horas: int = 1, minutos: int = 1, segundos: int = 1):
    total = (horas*3600) + (minutos*60) + segundos
    print("Total en segundos:", total)