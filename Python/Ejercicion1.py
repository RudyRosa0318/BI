#Programa
#Objetivo: Evaluar La Nota del Alumno
#Autor:Rudy Rosa
#Fecha:23/01/2020

def evaluarNota(nota):
    '''
    Retorna un mensaje dependiendo del valor de la nota
    
    Parametros
    nota: El Valor de la Nota a evaluar
    '''

    if nota >= 91 and nota <= 100:
        print('¡Felcidades Excelente Nota!')
    elif nota >= 80 and nota < 91:
        print('Muy Buena Nota')
    else:
        print('Nota Baja')
       


