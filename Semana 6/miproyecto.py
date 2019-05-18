#esto es un proyecto que usa otro modulo

from archivo1 import   suma_resta

resultado = suma_resta(a=10, b=3,c=3)

resultado =suma_resta(10,3,2)

print(resultado)

from archivo2 import mi_lista
from archivo2 import mi_diccionario


print("esto es un ejemplo")

from subfolder.archivo3 import Pato

donald = Pato()
caminante = donald.camina()

print(caminante)

mi_lista.append(7)

pass
