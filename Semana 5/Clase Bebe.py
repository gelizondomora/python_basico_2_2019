#Crear una clase Bebe

#Declarar 4 acciones: respirar, comer, llorar, dormir

#Similiar un dia normal del bebe

class Bebe():

    def __init__(self,nombre,edad=0):
        self.nombre = nombre
        self.edad = edad
    def respirar(self):
        print("Estoy respirando")

    def comer(self):
        print("Panza llena corazon contento")

    def llorar(self):
        print("AAHHHH!")

    def dormir(self):
        print("ZZZZZZZ")

    def crecer(self, edad=1):
        self.edad+= edad
        print("Hola soy {}, mi edad del bebe es: {}".format(self.nombre,self.edad))

bebe =Bebe("Jokic")

print("El nombre del bebe es:", bebe.nombre)

print(bebe.crecer(4))

print("En la manaña")
bebe.respirar()
bebe.comer()
bebe.llorar()

print("En la tarde")
bebe.respirar()
bebe.comer()
bebe.llorar()
bebe.dormir()

print("En la noche")
bebe.dormir()


bebe.crecer()