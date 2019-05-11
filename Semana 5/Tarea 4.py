#Suponga que se tiene una lista de listas que se tiene diversas cantidades por persona.
# La primera columna con números representa la cantidad en miles de colones que tienen en la cuenta del banco,
# la segunda columna la cantidad en crédito en miles de colones y la tercer columna en miles de colones en deuda.

hoja_calculo = [
    ['carlos', 54.54,6.57,3.64],
    ['juan', 5.54,9.57,4.64],
    ['luis', 9.54,7.57,1.64] ,
]

#Suponga que se dispone de una función que procesa la lista para obtener la transpuesta(cambiar las columnas por las filas)

def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]

b = transpuesta(hoja_calculo)

#Resultado
#[['carlos', 'juan', 'luis'],
 #[54.54, 5.54, 9.54],
 #[6.57, 9.57, 7.57],
 #[3.64, 4.64, 1.64]]

#Parte 1

#Contruya un diccionario de funciones matematicas (utilizando funciones lambda) entre todos los números de la lista tales como:
# Promedio

# La suma

# La multiplicación


b[1] = list(map(lambda x: x/10, b[1]))




##Parte 2
#Obtenga utilizando el diccionario de funciones:
#1. El promedio de la cantidad miles de colones en débito: cuánto tienen en promedio todas las personas.
#2. La suma de todas las deudas
#3. la multiplicación de todos los crédito entre si

