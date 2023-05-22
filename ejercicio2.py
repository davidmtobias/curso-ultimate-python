from pprint import pprint

# 1. Eliminar los espacios en blanco de un string
# y devolver una lista con los carateres restantes


def quita_espacios(texto):
    return list(texto.replace(" ", ""))

    # return [char for char in texto if char != " "]

# 2. Contar en un diccionario cuanto se repite los caracteres de un string


def cuenta_caracteres(lista):
    diccionario = {}

    for char in lista:
        if char in diccionario:
            diccionario[char] += 1
        else:
            diccionario[char] = 1
    return diccionario

# 3. Ordenar las llaves de un diccionario
# por el valor que tienen y devolver una lista
# que contiene tuplas [("a", 3), ("b", 4), etc..]


def ordena(diccionario):

    # # Ordenar un diccionario
    # return sorted(
    #     diccionario.items(),
    #     key=lambda key: key[1],
    # 	  reverse= True
    # )

    # Convertimos el diccionario a una matriz para poder ordenarla con sort
    matriz = []

    for item in diccionario:		# Iteramos las llaves
        matriz.append([item, diccionario[item]])

    # Ordenamos por el númeo de repeticiones
    matriz.sort(key=lambda el: el[1])

    # Convertimos un array de arrays en un array de tuplas
    tuplas = []
    for item in matriz:
        tuplas.append(tuple(item))

    # Devolvemos el array de tuplas
    return tuplas

# 4. De un listado de tuplas, devolver las tuplas que tenga el mayor valor


def mayores_tuplas(lista):
    tuplas = []
    valor = 0
    for tupla in lista:
        if tupla[1] > valor:
            tuplas.clear()
            tuplas.append(tupla)
            valor = tupla[1]
        elif tupla[1] == valor:
            tuplas.append(tupla)

    return tuplas


# 5. Crear un mensaje que diga:
# Los caracteres que más se repiten con 4 repeticiones son:
# -C
# -D

def mensaje_resumen(tuplas):
    repeticiones = tuplas[0][1]
    print(
        f"Los caracteres que más se repiten con {repeticiones} repeticiones son:")
    for tupla in tuplas:
        print(f"- {tupla[0].upper()}")


# 6. Juntar la solucion de los ejercicios anteriores
# para encontrar los caracteres que más se repiten
# de un sring

def caracteres_repetidos(string):
    lista = quita_espacios(string)
    diccionario = cuenta_caracteres(lista)
    tuplas = ordena(diccionario)
    tuplas_mayor = mayores_tuplas(tuplas)
    mensaje_resumen(tuplas_mayor)


caracteres_repetidos("aaaaaaEn un llugak lañsdf alksdfj asdf")
