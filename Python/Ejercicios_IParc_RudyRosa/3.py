# Objetivo: Desarrollo Guia Aprendizaje Python
# Autor: Rudy R. Rosa
# Fecha: 9-febrero-2020

import math
def primo(numero):
    """
    Factor de un numero primo, consta de los numero que son divisibles entre el mismo y 
    su divisor es un numero entero

    Param:
    numero: es el valor a mostrar y buscar sus numeros primos
    """
    assert numero >= 2
    for i in range(2, numero):
        if numero % i == 0:
           print(i)
    return 0
print(primo(13195))
