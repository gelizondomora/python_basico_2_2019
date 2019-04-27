#Cuantos articulos voy a comprar

verduras = ["papas","cebollas","ajos", "tomate"]
carnes = ["mortadela", "pollo", "costilla de cerdo"]
frutas = ["piña", "naranja", "sandia"]
limpieza = ["jabon", "cloro", "shampoo"]

lista_general_compras = []
lista_general_compras.append(verduras)
lista_general_compras.append(carnes)
lista_general_compras.append(frutas)
lista_general_compras.append(limpieza)

mi_lista = []
for x in lista_general_compras:
    mi_lista.extend(x)
print(len(mi_lista))

pass
