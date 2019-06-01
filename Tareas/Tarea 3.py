#Escriba un programa que permita crear una lista de palabras.
# Para ello, el programa tiene que pedir un número y luego solicitar ese número de palabras para crear la lista.
# Por último, el programa tiene que escribir la lista.

num_palabras= int(input("Dígame cuántas palabras tiene la lista: "))
item = 1
todos =[]
list(todos)
if num_palabras > 0:

    while item <= num_palabras:
        palabra= input("Dígame la palabra "+str(item))
        list(palabra)
        todos.insert(item,palabra)
        item =item+1
    print("La lista creada es: ",todos)
else:
    print("Imposible!")


#Escriba un programa que permita crear una lista de palabras y que, a continuación,
#pida una palabra y diga cuántas veces aparece esa palabra en la lista.


num_palabras= int(input("Dígame cuántas palabras tiene la lista: "))
item = 1
todos =[]
list(todos)
if num_palabras > 0:

    while item <= num_palabras:
        palabra= input("Dígame la palabra "+str(item))
        list(palabra)
        todos.insert(item,palabra)
        item =item+1
    print("La lista creada es: ",todos)
    busqueda = input("Dígame la palabra a buscar: ")
    contador = 0
    for x in todos:
        if x == busqueda:
            contador += 1
        else:
            print("La palabra ",busqueda, "no aparece en la lista.")
            break
    if contador == 1:
        print("La palabra ", busqueda, " aparece", contador, "vez en la lista.")
    elif contador != 1 and contador != 0:
        print("La palabra ",busqueda," aparece", contador,"veces en la lista.")
else:
    print("Imposible!")
