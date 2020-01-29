# Programa: Ejercicio2.py
# Objetivo: Evaluar conocimiento aprendidos Fibonacci
# Autor: Rudy Rosa
# Fecha: 29/enero/2020

import math

def suma_fibonacci(numero):
    """
    retorna la suma de toos los numeros pares que se generan
    en la sucesion de fibonacci.
    la sucesion se realiza hasta un numero menor que el valor dado

    Param:
    numero : el valor maximo a generar en la sucesion.
    """
    suma = 0
    #x/y/z... variable cuando sea un calculo
    x = 1 #representa el valor actual de la sucesion
    y = 2 #representa el valor siguiente en la sucesion
    while x <= numero:
        if x % 2 == 0:
            suma += x
        #asignacion multiple
        x, y = y, x + y
    return suma

if __name__ == "__main__":
    print(suma_fibonacci(4000000))
