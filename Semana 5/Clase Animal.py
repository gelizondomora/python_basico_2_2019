class Animal:
    def __init__(self, e, a):
        self.especie = e
        self.edad = a

    def correr(self):
        print('Soy un {}. '
              'Estoy corriendo'.format(self.especie))

    def crecer(self, edad=0):
        if (self.edad + edad) > 14:
            self.edad += edad
            self.vivo = False

        else:
            self.edad += edad
            self.vivo = True

perro = Animal('perro', 5)

print("hola soy un {} "
      "tengo {} años".format(perro.especie,
                        perro.edad))

perro.crecer(10)

print("hola soy un {} "
      "tengo {} años".format(perro.especie,
                        perro.edad))


if perro.vivo:
    print("hola soy un {} "
          "tengo {} años".format(perro.especie,
                            perro.edad))
else:
    print('...Me morí... RIP')