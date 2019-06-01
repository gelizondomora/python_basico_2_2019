#Crear líneas de código en Python que calcule el promedio de los valores contenidos en una lista.

import numpy as np

mis_valores = [5,6,10,13,3,4]

promedio = np.mean(mis_valores)

print(promedio)

#Escriba un código en python que determine cual grupo de personas contiene la mayor de todas las alturas de todas las personas



todos = [

[177,145,167,190,140,150,180,130], # grupo 1

[165,176,145,189,170,189,159,190], # grupo 2

[145,136,178,200,123,145,145,134], # grupo 3

[201,110,187,175,156,165,156,135] # grupo 4

]

#grupos = ["Grupo 1","Grupo 2","Grupo 3","Grupo 4"]
#diccionario = dict(zip(grupos,todos))

mas_alto = max(*todos)


print(todos.index(mas_alto))