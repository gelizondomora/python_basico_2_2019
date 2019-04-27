# Utilizando pasos 1, 2, 4

verduras = ["papas","cebollas","ajos", "tomate"]
carnes = ["mortadela", "pollo", "costilla de cerdo"]
frutas = ["piña", "naranja", "sandia"]
limpieza = ["jabon", "cloro", "shampoo"]
lista_general_compras = []
lista_general_compras.append(verduras)
lista_general_compras.append(carnes)
lista_general_compras.append(frutas)
lista_general_compras.append(limpieza)

verduras.append("chile")
frutas.append("mango")

del verduras[0:5]

print(lista_general_compras)

pass

a= tuple("1",2,3,4)

print(a[0,2])