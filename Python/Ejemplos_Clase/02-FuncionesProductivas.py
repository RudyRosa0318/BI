# -*- coding: utf-8 -*-
# Programa: 02-FuncionesProductivas.py
# Objetivo: Evaluar la utilización de funciones productivas
# Autor: H´ector Sabillón
# Fecha: 27/enero/2020
import math  # Librería de funciones matemáticas avanzadas


def calculo_area_circulo(radio):
    """
    Retorna el área de un círculo.

    Parámetros:
    radio: el valor del radio del círculo.
    """
    return math.pi * radio ** 2


def valor_absoluto(x):
    """
    Retorna el valor absoluto de un número real.

    Parámetros:
    x: el valor del número a calcular su valor absoluto.
    """
    if x < 0:
        return x * -1
    else:
        return x


def distancia_entre_dos_puntos(x1, x2, y1, y2):
    """
    Retorna la distancia entre dos puntos cardinales.

    Parámetros:
    x1, y1: el valor de primer punto.
    x2, y2: el valor del segundo punto.
    """
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def doblar_valor_elementos(una_lista):
    """
    Retorna los valores de los elementos de una lista
    multiplicados por el número 2.

    Parámetros:
    una_lista: lista de elementos cuyos valores se duplicarán.
    """
    for valor in range(len(una_lista)):
        una_lista[valor] = una_lista[valor] * 2

    return una_lista


# Probar las funciones
print('La distancia entre los puntos es: ',
      distancia_entre_dos_puntos(1, 2, 9, 10))
print('El área del círculo es: ', calculo_area_circulo(2.5))
print('El valor absoluto de -123 es: ', valor_absoluto(-123))
mi_lista = list(range(10))
print(' El valor de la lista doble es: ', doblar_valor_elementos(mi_lista))
