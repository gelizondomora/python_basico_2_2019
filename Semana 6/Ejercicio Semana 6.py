#Definir la estructura de datos
#Definir una funcion que permita agregar datos del paciente
#
identificacion = 0
nombre = []
apellido =None
telefono = None
direccion = None
enfermedades = None
medicamentos = None



paciente = {}

agenda = []


def ingresar_paciente():
    identificacion = input("Ingrese identificacion del paciente")
    agenda.append(identificacion)
    nombre = input("Ingrese nombre de paciente")
    agenda.append(identificacion)
    apellido= input("Ingrese apellido del paciente")
    telefono = input("Ingrese telefono del paciente")
    direccion = input("Ingrese direccion del paciente")
    enfermedades = input("Ingrese enfermedades del paciente")
    medicamentos = input("Ingrese medicamentos del paciente")
    return paciente.update({identificacion:{"Nombre": nombre,
                          "Apellido":apellido,
                          "Telefono":telefono,
                          "Direccion":direccion,
                          "Enfermedades": enfermedades,
                          "Medicamentos": medicamentos}})


agregar_paciente = input("Quiere agregar otro paciente? Y/N")

if agregar_paciente == "Y":
    ingresar_paciente()
elif agregar_paciente == "N":
    pass


pass
