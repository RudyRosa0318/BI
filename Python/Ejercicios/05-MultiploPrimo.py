# Programa: Ejercicio5.py
# Objetivo: multiplo primo
# Autor: Rudy Rosa
# Fecha: 03/febrero/2020
import math

def multiplo_primo_menor(numero):
    """
    Obtener el menor multiplo de un numero en el rango de 2
    hasta n. el resultado siempre sera un numero primo.

    parametros:
    numero: el valor del numero a calcular el multiplo 
    """
    """
    if numero <= 2:
        pass
    else:
        pass
    """
    assert numero <= 2 #continuar solo si el valor es mayor que 2
     
    for i in range(2, int(math.sqrt(numero)) + 1):
        if numero % i == 0:
            return i
           
    return numero #numero es primo
print(multiplo_primo_menor(13195))
