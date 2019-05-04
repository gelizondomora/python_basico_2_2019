# Crear ina agenda de contactos utilizando diccionarios

#Nombres      Telefono     Email
#Juan Perez   83013040     jperez@gmail.com
#Carlos Rojas 87001030      crojas@hotmail.com
#Ana Marin    9100013       ana@marin.com




agenda = {"Juan Perez": {"telefono": 83013040, "correo": "jperez@gmail.com"},
            "Carlos Rojas": {"telefono": 87001030, "correo": "crojas@hotmail.com"},
            "Ana Marin": {"telefono": 9100013, "correo": " ana@marin.com"}
          }

# cuantas personas hay en la agenda

print(len(agenda["Juan Perez"]))

#Cuales son los nombres de los contactos

print(list(agenda.keys()))

#Utilizando la agenda imprima las informaciones de cada contacto.
# Nombre: Juan Perez Telefono: 83013040 Correo:jperez@gmail.com


for x in agenda.keys():
    print("Nombre:",x ," Telefono: ", agenda[x]["telefono"], " Correo: ",agenda[x]["correo"])


# Otras maneras

#keys()

for persona in agenda.keys():
    print("Nombre:", persona,
          " Telefono: ", agenda[persona]["telefono"],
          " Correo: ", agenda[persona]["correo"])

#items()

for persona, info in agenda.items():
   print("Nombre:", persona,
         " Telefono: ", info["telefono"],
         " Correo: ", info["correo"])


##Suponga que Juan Perez cambio de telefono, ahora tiene 2

agenda["Juan Perez"]["telefono"] = [6310111, 23333333]

#Nuevo contacto Sofia Telefono 333333 Correo sofia@gmail.com

#Opcion 1 crear un diccionario para Sofia

sofia ={"telefono" : 3333333,
        "correo" : "sofia@gmail.com"}
agenda["sofia castro"] = sofia

#Opcion 2

agenda.update({"sofia alfaro": sofia})
pass