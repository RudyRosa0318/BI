# Programa: Ejercicio2.py
# Objetivo: Evaluar conocimiento aprendidos
# Autor: Rudy Rosa
# Fecha: 27/enero/2020

import math

"""suma = 0
for i in range (1,1000):
    residuotres = i % 3
    residuocinco = i % 5
    
    if residuotres == 0 or residuocinco == 0:
        print(i)
        suma = i + suma
        
print(suma)"""
#########################################
#Ejercicios Ing
def suma_de_multiplos (numero):
    """
    retorna la suma de los multiplos de 3 o 5

    Param: 
    numero: el valor maximo -1 a calcular
    """
    suma = sum(x for x in range (numero) if (x % 3 == 0 or x % 5 == 0))
    return suma

if __name__ == "__main__":
    print(suma_de_multiplos(1000))
    
    
    

 

    


