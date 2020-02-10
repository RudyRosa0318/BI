#Programa: Ejercicio4
# Objetivo: Desarrollo Guia Aprendizaje Python
# Autor: Rudy R. Rosa
# Fecha: 9-febrero-2020

import math
def palindromo(numero):
    mayorPalin = 0
    mayor = 0

    for i in range(1,100):
        for ii in range(1,100):
            multi = i * ii
            print(i," x ", ii, " = ", multi)
            a = multi
            voltear= 0
            while a > 0:
                residuo = a % 10
                voltear = (voltear * 10) + residuo
                a //= 10
            if voltear == multi:
                 mayorPalin = multi
            if mayorPalin > mayor:
                mayor = mayorPalin
    
    print("El palindromo mayor es: ", mayor)
