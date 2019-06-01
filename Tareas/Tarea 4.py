#Suponga que se tiene una lista de listas que se tiene diversas cantidades por persona.
# La primera columna con números representa la cantidad en miles de colones que tienen en la cuenta del banco,
# la segunda columna la cantidad en crédito en miles de colones y la tercer columna en miles de colones en deuda.
import math

from functools import reduce


hoja_calculo = [
    ['carlos', 54.54,6.57,3.64],
    ['juan', 5.54,9.57,4.64],
    ['luis', 9.54,7.57,1.64] ,
]

def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]

b = transpuesta(hoja_calculo)
b #sea b la tabla resultante luego de aplicar transpuesta





#Parte 1
#Contruya un diccionario de funciones matematicas (utilizando funciones lambda) entre todos los números de la lista tales como:
#Promedio
#La suma
#La multiplicación

#promedio = reduce(int(lambda x, y: x + y, b) / len(b))


diccionario_funciones ={"Promedio":lambda x: sum(x)/len(x),
                        "Suma":lambda x,y: sum(x)}
                       # "Multiplicacion":lambda x,y: }



#Parte 2
#Obtenga utilizando el diccionario de funciones:
#1. El promedio de la cantidad miles de colones en débito: cuánto tienen en promedio todas las personas.
#2. La suma de todas las deudas
#3. la multiplicación de todos los crédito entre si


print()



#Parte 3
#Actualice (en la tabla general)los valores de los créditos aplicando un impuesto del 20% (esto es multiplicar por 1.2)
# a toda la fila de créditos usando el diccionario de funciones.