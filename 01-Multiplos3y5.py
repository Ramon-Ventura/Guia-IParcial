# Programa: 01-Multiplos3y5
# Objetivo: Sumar todos los multiplos de 3 o 5
# Autor: Ramon Humberto Ventura
# Fecha: 02/Febrero/2020

def sum_multiplos(numero):
    '''
    Retorna la suma de los multiplos de 3 o 5 del numero ingresado

    Parametros:
    numero: Valor del numero ingresado, del cual obtendremos sus multiplos de 3 o 5
    '''
    suma = 0 # valor de la sumatoria de los multiplos.
    for x in range(1,numero):
        if x % 3 == 0 or x % 5 == 0:
            suma = suma + x
    return suma


if __name__ == "__main__":
    print('La suma de los multiplos de 3 o 5 es: ',sum_multiplos(1000))
