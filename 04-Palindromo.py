# Programa: 04-Palindromo.py
# Objetivo: Obtener el palindromo mayor del producto de dos numeros de tres digitos
# Autor: Ramon Ventura
# Fecha: 01/Enero/2020
def palindromo():
    '''
    Retorna el palindromo mas grande del producto de dos numeros de tres digitos
    '''
    mayor = 0
    for x in range(100,1000):
        for y in range(100,1000):
            if str(x * y) == str(x * y)[::-1]:
                if x * y > mayor:
                    mayor = x * y
    return mayor


if __name__ == "__main__":
    print(palindromo())
