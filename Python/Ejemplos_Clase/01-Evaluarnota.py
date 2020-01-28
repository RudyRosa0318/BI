# -*- coding: utf-8 -*-
# Programa: 01-EvaluarNota.py
# Objetivo: Evaluar la nota de un alumno
# Autor: Héctor Sabillón
# Fecha: 23/enero/2020


def evaluarNota(nota):
    '''
    Retorna un mensaje dependiendo del valor de la nota.

    Parámetros:
    nota: el valor de la nota a evaluar.
    '''
    if nota >= 91 and nota <= 100:
        print('¡Felicidades por tu excelente nota!')
    elif nota >= 80 and nota < 91:
        print('¡Muy buena nota')
    elif nota >= 70 and nota < 80:
        print('Pasaste... pero podrías hacerlo mejor')
    elif nota < 70 and nota >= 0:
        print('Hay que estudiar más y jugar menos...')
    else:
        print('¡El valor de la nota es incorrecta!')


# Pedir la nota al usuario
nota_a_evaluar = int(input('Ingrese el valor de la nota: '))
evaluarNota(nota_a_evaluar)
