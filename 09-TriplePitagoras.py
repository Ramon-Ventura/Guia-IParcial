# Programa 09-TriplePitagoras.py
# Guia: I-Parcial
# Objetivo: Encontrar un triple de pitagoras que cumpla con la condicion a+b+c = 1000
# Autor: Ramon Ventura
# Fecha: 02/Febrero/2020

def triple_pitagorico(solucion):
    '''
    retorna el triple de pitagoras que cumpla con la condicion establecida

    Parametros:
    solucion: valor de la solucion de la ecuacion de a + b + c
    '''
    c = 0 # valor de la hipotenusa (c)
    bandera = False # valor que indica que el resultado ha sido encontrado
    for a in range(1,int(solucion/3)):
        for b in range(a,int(solucion/2)):
            c = solucion - a - b
            if a ** 2 + b ** 2 == c ** 2:
                bandera = True
                break
        if(bandera):
            break
    return str(a)+' + '+str(b) + ' + ' + str(c) + ' = ' + str(a+b+c) 


print(triple_pitagorico(1000)) 