# Programa: Ejercicios3.py
# Objetivo: Evaluar conocimiento aprendidos
# Autor: Rudy Rosa
# Fecha: 27/enero/2020

import math

suma = 0
for i in range (1,10):
    residuotres = i % 3
    residuocinco = i % 5
    
    if residuotres == 0 or residuocinco == 0:
        print(i)
        suma = i + suma
        
print(suma)

        

    
    
    

 

    


