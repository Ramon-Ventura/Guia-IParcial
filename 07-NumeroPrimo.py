# Programa 07-NumeroPrimo.py
# Guia: I-Parcial
# Objetivo: Obtener el numero primo 20,001
# Autor: Ramon Ventura
# Fecha: 02/Febrero/2020

def numero_primo(rango):
    '''
    Retorna el primo n de la infinita lista de numeros primos consecutivos

    Parametros:
    rango: valor del limite de la lista de numeros primos consecutivos
    '''
    x = 1 # primer numero primo de la lista
    lista = list(range(1,(rango*15)+1)) # lista de numeros de los cuales se eliminaran los que no son primos
    while lista[x] ** 2 < rango*15:
        y = x
        while y < len(lista):
            if lista[y] % lista[x] == 0 and lista[y] > lista[x]:
                del (lista[y])
            y += 1
        x += 1
    return 'El primo ' + str(rango) + ' es ' + str(lista[rango])

    
if __name__ == "__main__":
    print(numero_primo(20001))