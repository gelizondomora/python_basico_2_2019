#Crear una funcion que agregue contactos  la agenda

agenda = {"Juan Perez": {"telefono": 83013040, "correo": "jperez@gmail.com"},
            "Carlos Rojas": {"telefono": 87001030, "correo": "crojas@hotmail.com"},
            "Ana Marin": {"telefono": 9100013, "correo": " ana@marin.com"}
          }

def add_contact(nombre,telefono,correo):
    agenda.update({nombre: {"telefono": telefono,"correo": correo}})

    #Otra manera
    #agenda[nombre] = {"telefono" : telefono,
    #                   "correo" : correo}
pass





