# para Crear nuevos tipos de datos

class First:
    def __init__(self):  #Metodo especial que nos permite inicializar o controlar_nuestra class
        print("Contructor ejecutado")

f = First()



#*****************************************************************************************************

#Crear un pato


class Duck:

    def __init__(self,nombre):
        self.duck_nombre =nombre # variable/atributo interna creada para el objeto.

    def quack(self):
        print("Quaaack")

    def walk(self):
        print("Walks like a duck")

donald = Duck("Donald")

donald.quack()
donald.walk()

print("Cual es tu nombre? ", donald.duck_nombre)
pass
