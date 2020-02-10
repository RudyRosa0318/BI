#Programa: Ejercicio2
# Objetivo: Desarrollo Guia Aprendizaje Python
# Autor: Rudy R. Rosa
# Fecha: 9-febrero-2020

def fibonacci(numero):
    """
    Encuentra la suma de el actual numero y el anterior
    sumando los terminos que sean pares

    Param: 
    numero: este numero demuestra hasta donde llegara la secuencia con un numero final.
    """
    suma = 0
    x = 1
    y = 2
    while x <= numero:
        if x % 2 == 0:
           suma += x
        x ,y = y, x + y
    return suma
if __name__ == "__main__":
    print(fibonacci(4000000))

