import random
import math
import pandas as pd


fuerza_del_motor = random.randint(0,9)

class misc:
    def __repr__(self):
        # return the clase name
        return self.__class__.__name__

    def __str__(self):
        # return the clase name
        return self.__class__.__name__


class Camion(misc):
    fuerza_del_motor = random.randint(0, 9)
    def Rendimiento(self):
        rendimiento = 2*fuerza_del_motor + 1
        return rendimiento

class Tractor(misc):
    fuerza_del_motor = random.randint(0, 9)
    def Rendimiento(self):
        rendimiento = math.floor(math.log(2)*fuerza_del_motor)
        return rendimiento

class Sedan(misc):
    fuerza_del_motor = random.randint(0, 9)
    def Rendimiento(self):
        rendimiento = 3*(fuerza_del_motor)**2
        return rendimiento

class Bus(misc):
    fuerza_del_motor = random.randint(0, 9)
    def Rendimiento(self):
        rendimiento = 5*(fuerza_del_motor)
        return rendimiento

camion = Camion()
tractor = Tractor()
sedan =Sedan()
bus = Bus()


meta = 1000
fila = [camion,tractor,sedan,bus]
df = pd.DataFrame(columns=fila)
contador = pd.array([0,0,0,0])
suma= pd.array([0,0,0,0])
cabeza = 0
index = 0
index_2 = 0

while cabeza <= meta:
    for i in fila:
        contador[index] = i.Rendimiento()
        index += 1
    suma = suma + contador
    df.loc[index_2] = suma
    index = 0
    index_2 += 1
    cabeza = max(suma)

ultima = df.tail(n=1)
ultima = ultima.astype('float64')
ultima = ultima.idxmax(axis=1)

if ultima.shape[0] > 1:
    print("Hay empate! El ganador es:", ultima.sum().sort()[0])
else:
    print("El ganador es :",ultima.to_string(index=False))

print("La eficiencia maxima por vehiculo es:\n",df.sum())

print("Se corrieron ",df.shape[0]," ciclos")


