# Programa 05-Divisible1a20.py
# Guia: I-Parcial
# Objetivo: Obtener la diferencia del cuadrado de la suma y de la suma de cuadrados de un rango en especifico.
# Autor: Ramon Ventura
# Fecha: 02/Febrero/2020

def cuadrado_de_la_suma(rango):
    '''
    Retorna el cuadrado de la suma del rango establecido.

    Parametros:
    rango: valor del rango ingresado (1 al 10, 1 al 20, etc).
    '''
    suma = 0
    for x in range(1,rango+1):
        suma = suma + x
    return suma ** 2


def suma_de_cuadrados(rango):
    '''
    Retorna la sumatoria de los cuadrados del rango establecido.

    Parametros:
    rango: valor del rango ingresado (1 al 10, 1 al 20, etc).
    '''
    suma = 0
    for x in range(1,rango+1):
        suma = suma + x ** 2
    return suma

diferencia = cuadrado_de_la_suma(10)-suma_de_cuadrados(100)
if diferencia < 1:
    diferencia = diferencia * -1
print('La diferencia es: ',diferencia)