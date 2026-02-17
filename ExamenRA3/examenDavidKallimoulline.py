import operaciones as op
from operaciones import info_argumentos, divisibles3, histograma, coste_envio

if __name__ == '__main__':
    print("Ejercicio 1")
    info_argumentos("Hola", "Adiós", 3)
    divisibles3(10, 9, 15, 35, 30, 15, 500, 300)
    histograma(5, 10, 15)
    print("Ejercicio 2")
    coste_envio(10, True)
    print("Ejercicio 3")
    horas = 5
    minutos = 10
    segundos = 1000
    try:
        op.convertir_segundos(horas, minutos, segundos)
    except TypeError:
        print("Uno de los valores introducidos no es un número")
