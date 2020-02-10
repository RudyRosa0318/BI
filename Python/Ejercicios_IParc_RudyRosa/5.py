#Programa: Ejercicio5
# Objetivo: Desarrollo Guia Aprendizaje Python
# Autor: Rudy R. Rosa
# Fecha: 9-febrero-2020

import math
def residuo_cero(numero):
    """
    La division de un numero, consta de dividendo ,divisor y residuos.
    sabiendo esto podemos encontrar con que numeros es divisible un valor ya que su residuo daria 0
    Param:
    numero: es el valor del numero a buscar sus residuo mientras se divide
    """
    for x in range (1,10):
        if(numero % x == 0):
            return x 
    return numero
if __name__ == "__main__":
    print(residuo_cero(2520))