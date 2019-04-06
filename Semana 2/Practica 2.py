#Crear un codigo que calcule las soluciones de la ecuacion cuadratica
#ax^2 + bx + c = 0
#x1 = ((-b +(b^2-4ac)^1/2)/2a
#x2 = ((-b -(b^2-4ac)^1/2)/2a

import math

a = float(input("Ingrese el valor de a "))
b = float(input("Ingrese el valor de b "))
c = float(input("Ingrese el valor de c "))

discriminante = (b**2)-4*a*c

if discriminante < 0:
    root = math.sqrt(-discriminante)*complex(0,1)
else:
    root = math.sqrt(discriminante)


x1 = (-b + root)/2*a
x2 = (-b + root)/2*a

print(x2,x1)


