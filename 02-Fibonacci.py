# Programa: 02-Fibonacci
# Guia: I-Parcial
# Objetivo: Encontrar la sumatoria de los terminos pares de la secuencia de fibonacci
# Autor: Ramon Humberto Ventura
# Fecha: 02/Febrero/2020

def fibonacci(numero):
    '''
    Retorna el resultado de la serie del fibonacci de acuerdo al indice

    Parametros:
    numero: valor del indice de la serie del fibonacci
    '''
    if numero == 1:
        return 1
    elif numero == 2:
        return 2
    else:
        return fibonacci(numero - 1) + fibonacci(numero - 2)


x = 1 # numero de elementos de la serie de fibonacci
suma = 0 # valor de la sumatoria de los terminos pares del fibonacci
while fibonacci(x) < 4000000:
    if fibonacci(x) % 2 == 0:
        suma = suma + fibonacci(x)
    x += 1
print(suma)