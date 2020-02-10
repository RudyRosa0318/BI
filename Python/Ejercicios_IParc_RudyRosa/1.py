# Programa: Ejercicio1
# Objetivo: Desarrollo Guia Aprendizaje Python
# Autor: Rudy R. Rosa
# Fecha: 9-febrero-2020

def multiplos(numero):
    """
    Encontrar la suma de los multiplos de 3 o 5

    Param: 
    numero : el rango a calcular los multiplos
    """
    suma = sum(x for x in range(numero) if(x % 3 == 0 or x % 5 == 0))
    return suma

if __name__ == "__main__":
    print("la suma es de", multiplos(1000))    