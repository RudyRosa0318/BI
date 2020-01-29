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
    elif nota >= 70 and nota < 80:
        print('Pasaste... pero podrias hacerlo mejor')
    elif nota < 70 and nota >= 0:
        print('Hay que estudiar más y jugar menos')
    else:
        print('El valor de la nota es incorrecto')
    
#pedir la nota al usuario
nota_a_evaluar = int(input('Ingrese la valor de la nota: '))
evaluarNota(nota_a_evaluar)


