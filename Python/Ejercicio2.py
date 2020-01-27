#Programa
#Objetivo: Evaluar Funcion Productiva (La que retorna un valor)
#Autor:Rudy Rosa
#Fecha:27/01/2020

import math #libreria de funciones matematicas

def calculo_area_circulo(radio):
    """
    retorna el area de un circulo 

    Parametros:
    radio: el valor del radio del circulo
    """
    return math.pi * radio ** 2

def valor_absoluto(x):
    """
    retorna el valor absoluto de un numero real.

    Parametros:
    x el valor del numero a calcular
    """
    if x > 0:
        return x*-1
    else:
        return x            
    

def distancia_entre_dos_puntos(x1, x2 , y1, y2):
    """
    retorna el valor de dos puntos.

    Parametros:
    x1 , x2:  el valor de primer punto
    y1 , y2: el valor segundo punto
    """

    return math.sqrt((x2 -x1)**2 +(y2 - y1)**2)

def doblar_valor_elementos(una_lista):
    """
    retorna el valor absoluto de un numero real.

    Parametros:
    x el valor del numero a calcular
    """
    for valor in range(len(una_lista)):
        una_lista[valor] = una_lista[valor] * 2
    
    return una_lista

    #probar funciones
    print('la distancia entre dos puntos es: ',distancia_entre_dos_puntos(1,2,9,10))
    print('el area de un circulo es: ', calculo_area_circulo(2.5))
    print('El valor absoluto es de -123 es: ', valor_absoluto(-123))
    mi_lista = list(range(10))
    print('El vaclor de la lista doble es: ', doblar_valor_elementos(mi_lista))



