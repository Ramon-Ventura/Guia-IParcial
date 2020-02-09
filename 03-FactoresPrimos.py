# Programa: 03-FactoresPrimos.py
# Guia: I-Parcial
# Objetivo: Obtener el factor primo mas grande de 600, 851,475,143
# Autor: Ramon Ventura
# Fecha: 01/Enero/2020

def factores_primos(numero):
    '''
    Retorna el factor primo mas grande de un numero

    Parametros:
    numero: representa el valor por descomponer a sus factores primos
    '''
    x = 2 # valor primo inicial para comprobar si es divisible
    mayor = 0 # almacena el factor primo mas grande del numero
    contador = 0 # verifica si los divisores del numero son factores primos
    while numero > 1:
        if numero % x == 0:
            for y in range(1,x+1):
                if x % y == 0:
                    contador += 1
            if contador == 2:
                print(x)
            contador = 0
            numero = numero / x
            mayor = x
        x += 1
    return mayor


if __name__ == "__main__":
    print('El primo mas grande es: ',factores_primos(600851475143))