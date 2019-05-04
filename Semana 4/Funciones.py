#Piezas de codigo para ser llamadas multiples veces

#funcion que sume 2 numeros

#posicion
def mi_suma(a, b):
    return a + b

#definicion
c = mi_suma(1,2)

#nombre
c = mi_suma(1,2)
pass



#Funciones Lambda

(lambda a,b : a+b)(3,4)

c= (lambda a,b : a+b)
print(c(3,4))
pass


#funcion Lambda sin parametros

(lambda : print("hola"))()