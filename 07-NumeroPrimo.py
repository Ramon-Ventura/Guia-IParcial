# Programa 07-NumeroPrimo.py
# Objetivo: Obtener el numero primo 20,001
# Autor: Ramon Ventura
# Fecha: 02/Febrero/2020

def numero_primo(rango):
    '''
    Retorna la cantidad n numeros primos consecutivos.

    Parametos:
    rango: Valor de la cantidad de numeros primos consecutivos
    '''
    numero = 1 # valor por verificar si es primo o no
    contador = 0 # valor que permite verificar la cantidad de divisores del respectivo numero
    primo = 0 # valor del rango de la cantidad de primos consecutivos
    x = 1 # valor que ira incrementando para verificar los divisores de cada numero
    while primo < rango-1:
        numero += 2
        while x <= numero:
            if numero % x == 0:
                contador += 1
            if contador > 2:
                break
            x += 2
        x = 1
        if contador == 2:
            primo += 1
            print (numero,primo+1)
            
        contador = 0
    return numero  

if __name__ == "__main__":
    print(numero_primo(20001))