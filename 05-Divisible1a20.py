# Programa 05-Divisible1a20.py
# Guia: I-Parcial
# Objetivo: Obtener el entero positivo mas pequeño divisible por los numeros del 1-20 
# Autor: Ramon Ventura
# Fecha: 02/Febrero/2020

def divisible(rango):
    '''
    Retorna el entero positivo mas pequeño divisible de acuerdo al rango ingresado.

    Parametros:
    rango: Rango de numeros enteros divisibles
    '''
    numero = rango
    contador = 0
    while contador != rango:
        contador = 0
        numero += rango 
        for x in range(1,rango+1):
            if numero % x == 0:
                contador += 1
    return numero


if __name__ == "__main__":
    print(divisible(20))
