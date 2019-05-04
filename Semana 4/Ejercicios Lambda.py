#Crear una calculadora que sume, reste, multiplique, divida, eleve, saque raiz de dos numeros

import math

suma = lambda x,y: x+y
resta = lambda x,y: x-y
divida =lambda x,y: x/y
multiplique =lambda x,y: x*y
potencia = lambda x,y: math.pow(x,y)
raiz = lambda x,y: math.pow(x,1/y)

x = 3
y = 2

lista_funciones = [suma,resta,multiplique,divida,potencia,raiz]
for mi_funcion in lista_funciones:
    print("Resultado = ", mi_funcion(x,y))

#Crear un diccionario de funciones que haga operaciones aritmeticas

dict_funciones = {"suma":lambda x,y: x+y,
                  "resta" :lambda x,y: x-y,
                  "divida":lambda x,y: x/y,
                  "multiplique" :lambda x,y: x*y,
                  "potencia": lambda x,y: math.pow(x,y),
                  "raiz": lambda x,y: math.pow(x,1/y)}

print("Usando diccionarios")
for f in dict_funciones.keys():
    print("Resultado = ", dict_funciones[f](x,y))

print("Usando values")
for f in dict_funciones.values():
    print("Resultado = ", f(x,y)
