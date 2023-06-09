##########################
# Seccion 2: Tipos básicos
##########################

# Strings

from pprint import pprint
nombre_curso = "Ultimate Python"
descripcion_curso = """
Ultimate Python,
este curso contempla todos los conocimientos
que necesitas aprender para 
un trabajo como programador.
"""
print(nombre_curso, descripcion_curso)

len(nombre_curso)   # => 15 Número de caracteres
nombre_curso[0]     # => 'U'
nombre_curso[0:8]   # => 'Ultimate' Susbtring pos 0 hasta pos 7
nombre_curso[9:]    # => 'Python' Substring desde 9 hasta el final
nombre_curso[:8]    # => 'Ultimate' Substring desde al principio hasta pos 7
nombre_curso[:]     # => 'Ultimate Python

# Formato de string
nombre = "Michael"
apellido = "Singer"
# Entre llaves puedo usar cualquier expresión
nombre_completo = f"{nombre} {apellido[0]}"

# Métodos de string
animal = "orniTORRinco sibeRIANO"
animal.upper()        # => 'ORNITORRINCO SIBERIANO'
animal.lower()        # => 'ornitorrinco suberiano'
animal.capitalize()   # => 'Ornitorrinco siberiano'
animal.title()        # => 'Ornitorrinco Siberiano'

animal.strip()        # Quita espacios a izq y dcha
animal.lstrip()       # Quita espacios a izq
animal.rstrip()       # Quita espacios a dcha

animal.find("TORR")   # => 4 Busca índice en string. Si no encuentra: -1

animal.replace("TORR", "J")  # => 'orniJinco sibeRIANO"

"TORR" in animal      # => True
"TORR" not in animal  # => False

# Secuencias de escape
curso = "Ultimate \"Python\""  # => Ultimate "Python"
curso = "Ultimate \'Python\'"  # => Ultimate 'Python'
curso = "Ultimate \\Python\\"  # => Ultimate \Python\
curso = "Ultimate \nPython"    # => Salto de línea

# Números
numero = 2
decimal = 1.2
imaginario = 2 + 2j

1 + 3   # Suma
1 - 3   # Resta
1 * 3   # Multiplicación
1 / 3   # División
1 // 3  # Cociente
1 % 3   # Resto
2 ** 3  # Potencia

numero += 2  # Forma corta
numero -= 2
numero *= 2
numero /= 2

# Módulo Math
round(1.3)  # => '1' Redonndeo
round(1.7)  # => '2' Redonndeo
round(1.5)  # => '2' Redonndeo

abs(-34)  # => '34' Valor absoluto

# import math
# docs.python.org/library/math
math.ceil(1.1)  # => '2' Entero superior
math.floor(1.999)  # => '1' Entero inferior
math.isnan(23)  # => False. Comprueba que no es un número
math.pow(10, 3)  # => '1000' 10 elevado a 3
math.sqrt(9)    # => 3 Raíz cuadrada

# Conversión de tipos
int()
str()
float()
bool("")  # => False
bool("0")  # => True
bool(None)  # => False
bool(" ")  # => True
bool(0)  # => False

#############################
# Seccion 3: Control de flujo
#############################

# Comparadores lógicos
1 > 2
1 < 2
1 <= 2
1 >= 2
2 == 2
2 == "2"
2 != "2"
2 != 2  # => False

# if, else, elif
edad = 15
if edad > 54:
    print("Puede ver la película con descuento")
elif edad > 17:
    print("Puede ver la película")
else:
    print("No puedes entrar")

# Operador ternario
mensaje = "Es mayor" if edad > 17 else "Es menor"

# Operadores lógicos: son operaciones de cortocircuito
# Si de izquierda a deracha, algún valor determina la expresión
# no se siguen evaluando el resto de condiciones hacia la derecha

gas = True
encendido = True
edad = 18

if not gas and (encendido or edad > 17):
    print("Puedes avanzar")

# Cadena de comparadores
if 15 <= edad <= 65:
    print("Puedo continuar")

# For
for numero in range(5):
    print(numero)

# For else
buscar = 10

for numero in range(5):
    print(numero)
    if numero == buscar:
        print("Numero encontrado")
        break
else:
    print("No encontré el número")

# Iterables
# Listas, tuplas y strings, son iterables, es decir, se pueden recorrer con un for
for char in "Ultimate Python":
    print(char)

# While
comando = ""

while comando.lower() != "salir":
    comando = input("$ ")  # Solicita texto en consola
    print(comando)

# Loop infinito
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break  # Agregar condición de salida para poder romper el loop infinito

# Loop anidado: Tratar de evitarlos salvo que no quede más remedio.
# Con listas muy grandes consumen muchos recursos.
for j in range(3):
    for k in range(2):
        print(f"{j} {k}")


# Ejercicio: Calculadora
print("Bienvenidos a la calculadora")
print("Para salir escribe Salir")
print("Las operaciones son suma, multi, div y resta")

comenzar = True
acumulador = input("Ingresa número: ")

if acumulador == "Salir":
    comenzar = False
else:
    acumulador = int(acumulador)


while comenzar:
    operacion = input("Ingresa operación: ")
    if operacion == "Salir":
        break

    numero = input("Ingresa siguiente número: ")
    if numero == "Salir":
        break

    numero = int(numero)

    if operacion == "suma":
        acumulador += numero

    elif operacion == "multi":
        acumulador *= numero
    elif operacion == "div":
        acumulador /= numero
    elif operacion == "resta":
        acumulador -= numero
    else:
        print("Operación no conocida")
        break

    print(f"El resultado es {acumulador}")


#############################
# Seccion 4: Funciones
#############################

# Introducción
def hola():
    print("Hola Mundo!")


hola()

# Parámetros y argumentos


def hola(nombre, apellido):  # Parámetros
    print(f"Hola {nombre} {apellido}")


hola("Marcus", "Sheiner")  # Argumentos

# Argumentos opcionales


def hola(nombre, apellido="Strauss"):  # Parámetros
    print(f"Hola {nombre} {apellido}")


hola("Marcus")  # => "Hola Marcus Strauss"
hola("Marcus", "Tobías")  # => "Hola Marcus Tobías"

# Argumenos nombrados
# => Tengo que nombrar todos necesariamente
hola(apellido="Tobías", nombre="David")

# Xarg: Un iterable como argumento


def sum(*numeros):  # El * indica que 'números' es un iterable
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 4, 55, 67, 7)

# Kwargs: Argumentos clave-valor (key-word args)


def get_product(**datos):  # El ** indica que es un diccionario clave-valor
    print(datos)
    print(datos["id"], datos["name"], datos["desc"])


get_product(id="23",
            name="iPhone",
            desc="Esto es un iPhone")

# Return


def suma(a, b):
    resultado = a + b
    return resultado


suma(1, 3)

# Alcance:

saludo = "Hola global"


def saludar_local():
    saludo = "Hola mundo"


def saludar_global():
    global saludo  # Solo usarlo de manera excepcional. Mala pŕactica
    saludo = "Hola mundo"


saludar_local()
print(saludo)
saludar_global()  # Cambia la variable global
print(saludo)

# Depurando funciones
# Must!

# Ejercicio: Palíndromo


def es_palindromo(texto):
    texto = texto.lower()           # Convierto a minúsculas
    texto = texto.replace(" ", "")  # Quito espacios en blanco
    return texto[::-1] == texto     # Invierto el texto


texto = "Amo la paloma"
print(texto, es_palindromo(texto))


#############################
# Seccion 5: Tipos avanzados
#############################

# Listas
numeros = [1, 2, 3]
letras = ["a", "b", "c"]
booleans = [True, False, True, True]
matriz = [[0, 1], [0, 1]]
ceros = [0] * 10
alfanumerico = numeros + letras
# A list le tenemos que pasar un Iterable
rango = list(range(10))  # => 0 a 9
rango = list(range(1, 11))  # => 1 a 10
chars = list("hola mundo")  # => ['h', 'o', 'l', ....]

# Manipulando listas
mascotas = ["Tobi", "Dogy", "Sazam", "Copito"]
mascotas[0] 			# Recoge el primer elemento
mascotas[0] = "Dave" 	# Reasigna
mascotas[2:]			# Recoge desde la posición 2 al final
mascotas[-1]			# Último
mascotas[::2]			# Tomta de dos en dos
mascotas[1::2]			# Comienza desde posición 1 y de dos en dos hasta el final
mascotas[1:2:2]			# Comienza desde posición 1 y de dos en dos hasta el 2

numeros = list(range(21))
numeros[::2]			# Números pares
numeros[1::2]			# Números impares

# Desempaquetar listas
numeros = [1, 2, 3, 4, 5]
primero, *otros = numeros  # primero => 1, otros => [2, 3, 4, 5]
primero, segundo, *otros, penu, ultimo = numeros  # "otros" será Iterable

# Iterar listas
mascotas = ["Pelusa", "Pulga", "Tobi", "Rocky"]
for mascota in enumerate(mascotas):
    print(mascota)  # => Devuelve tuplas (0, 'Pelusa), (1, 'Pulga') ...
    print(mascota[0])  # => 0 1 ...
    print(mascota[1])  # => Pelusa Pulga ...

# Con índice
for indice, mascota in enumerate(mascotas):
    print(indice, mascota)  # => Devuelve 0 'Pelusa' ...

# Buscando elementos
mascotas = ["Pelusa", "Pulga", "Tobi", "Rocky", "Pulga"]

mascotas.index("Pulga")  # => 1
mascotas.index("Noexiste")  # => Error
if "Noexiste" in mascotas:
    mascotas.index("Noexiste")

mascotas.count("Pulga")  # => 2

# Agregando y eliminando elementos a un listado
mascotas = ["Pelusa", "Pulga", "Tobi", "Rocky", "Pulga"]

mascotas.insert(1, "Dave") 	# Ingresamos Dave en la posición 1
mascotas.append("Melvin") 	# Ingresamos Melvin al final
mascotas.remove("Pulga") 	# Elimina la primera ocurrencia
# Si queremos eliminar más de una ocurrencia tendremos que contar con count y ejecutar remove tantas veces
mascotas.pop()				# Elimino el último
mascotas.pop(1)			# Saca el elemento 1
del mascotas[1]				# Otra forma de eliminar el elemento 1
mascotas.clear()			# Vacía la lista

# Ordenando listas
numeros = [3, 55, 334, 4, 6, 76, 45]
numeros.sort()					# Ordena
numeros.sort(reverse=True)		# Orden descendente
sorted(numeros)					# Devuelve una NUEVA lista pero no modifica el original
sorted(numeros, reverse=True)  # Idem en orden descendente

usuarios = [[4, "David"], [1, "María"], [5, "Begoña"], [9, "Eladio"]]
usuarios.sort()		# Ordena según primer argumento

# Cambia la película, ordenamos según el segundo elemento
usuarios = [["David", 4], ["María", 1], ["Begoña", 5], ["Eladio", 9]]


def ordena(elemento):
    return elemento[1]


# No ponemos 'ordena()', solo 'ordena', porque queremos pasar la referencia y no ejecturla
usuarios.sort(key=ordena)
usuarios.sort(key=ordena, reverse=True)

# Buscamos una forma más elegante de pasar un función a sort

# Expresiones lambda (o funciones anónimas)
# usuarios.sort(key=lambda parametros: valorRetorno, reverse=True)
# Estas funciones anónimas son recomendables si las utilizamos solo una vez como en este caso
usuarios.sort(key=lambda el: el[1], reverse=True)

# Compresión de listas
# Sintaxis: nombres = [expresion for item in items]
usuarios = [["David", 4], ["María", 1], ["Begoña", 5], ["Eladio", 9]]

# moficación de lista (MAP)
# => ["David", "María", "Begoña", "Eladio"]
nombres = [usuario[0] for usuario in usuarios]

# filtrar usuarios con id > 2 (FILTER)
nombres = [usuario for usuario in usuarios if usuario[1] > 2]

# modificar + filtrar usuarios con id > 2
nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# Map y filter (alternativa a lo anterior)
# Los programadores que preferien la programación funcional prefieren map o filter
nombres = list(map(lambda usuario: usuario[0], usuarios))  # MAP
menosUsuarios = list(
    filter(lambda usuario: usuario[1] > 2, usuarios))  # FILTER

# Tuplas (paréntesis redondos)
# Una tupla es lo mismo que una lista, con la salvedad de que no se puede modificar
# La usamos cuando no queramos modificar sus elementos
# Las operaciones son las mismas que las de las listas salvo las que modifique la tupla
# Podemos: manipular, desempaquetar e iterar
numeros = (1, 2, 3) + (4, 5, 6)  # => (1, 2, 3, 4, 5, 6)

# Lista a Tupla. Tuple recibe cualquier cosa que sea Iterable
punto = tuple([1, 2])

# Para modificar una tupla, creo primero un lista en base a la tupla
lista_numero = list(numeros)

# Sets (conjuntos o grupos)
# Es una colección de datos que no se puede repetir y que tampoco está ordenada
primer = {1, 1, 2, 2, 3, 4}
# => {1, 2, 3, 4} Python quita los duplicados en el momento de usar el set
print(primer)

primer.add(5)
primer.remove(1)


primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
# Creaión de un set en base a una lista. Set recibe un Iterable.
segundo = set(segundo)

primer | segundo 	# Unión. Y elimina duplicados
primer & segundo 	# Intersección. Y elimina duplicados
primer - segundo  # Diferencia {1, 2} Al de la izq le quito los de la dcha
primer ^ segundo  # Diferencia simétrica. Devuelve todos menos la intersección

# Los sets no están ordenados, por lo tanto no puedo hacer:
segundo[1]  # NO PUEDO, pero si puedo ver si un elemento está en el conjunto
if 5 in segundo:
    print("El 5 está")

# Diccionarios (pares llave-valor)
# Solo acepta strings como llave
punto = {"x": 25, "y": 50}
punto["x"]  # => 25
punto["y"]  # => 50
punto[0] 			# Error, porque no son listas
punto["z"] = 45		# Añado nueva llave dinámicamente
punto["t"]			# Error porque la llave no existe

if "t" in punto:
    punto["t"]		# Pregunto primero y me ahorro el error

punto.get("x")  		# => 25
punto.get("y")  		# => 50
punto.get("z")  		# => None
punto.get("z", 97)  	# => 97 Por defecto si no existe
del punto["x"]			# Elimina llave y valor
del (punto["y"])  		# También tengo una función "del"

for valor in punto:		# Iteramos las llaves
    print(valor, punto[valor])

for valor in punto.items():
    print(valor)		# Devuelve tuplas ('x', 25) ...

for llave, valor in punto.items():  # Desempaquetamos las tuplas
    print(llave, valor)		# Devuelve tuplas: x 25

usuarios = [
    {"id": 1, "nombre": "David"},
    {"id": 2, "nombre": "María"},
    {"id": 3, "nombre": "Begoña"},
    {"id": 4, "nombre": "Eladio"}
]

for usuario in usuarios:
    print(usuario["nombre"])

# Operador de desempaquetado
lista = [1, 2, 3, 4]
print(lista)  # => [1, 2, 3, 4]
print(1, 2, 3, 4)  # => 1 2 3 4
print(*lista)       # => 1 2 3 4 Desempaqueto la lista
# Para listas ...
lista2 = [5, 6]
combinada = [*lista, *lista2]  # => [1, 2, 3, 4, 5, 6]
# => ['Hola', 1, 2, 3, 4, 'mundo', 5, 6]
combinada = ["hola", *lista, "mundo", *lista2]

# Para diccionarios
punto1 = {"x": 19}
punto2 = {"y": 15}
nuevoPunto = {**punto1, **punto2}  # => {'x': 19, 'y': 15}
# => {'x': 19, 'y': 15, 'z': 'mundo'}
nuevoPunto = {**punto1, **punto2, "z": "mundo"}
# => {'x': 19, 't': 'tiempo', 'y': 15, 'z': 'mundo'}
nuevoPunto = {**punto1, "t": "tiempo", **punto2, "z": "mundo"}
# Nota: Se asigna de derecha a izquierda. Si la llave ya existe, se reasigna el valor.


# Filas (First in first out FIFO)
# Trabajar con LISTAS puede ser muy costoso computacionalmente si quito el elemento de la izquierda y
# desplazo todos los demás una posición a la izquierda. Para ello uso deque.
# Con 4 elemento puedo trabajar con listas, pero con 100.000.000 debo usar deque.

# from collections import deque
fila = deque([1, 2])
fila.append(3)
fila.append(4)
fila.append(5)
fila.popleft()  # => Quito elementos a la izquierda
if not fila:  # Falsy: lista vacía, string vacía o cero
    print("Fila vacía")

# Pilas (Last In First Out) Ej: Historial de navegación
# Se puede implementar con LISTAS
pila = []
pila.append(1)
pila.append(2)
pila.append(3)
pila.pop()  # => retorna el último elemento
pila[-1]  # => Acceder al último elemento de la lista
if not pila:    # Falsy: lista vacía, string vacía o cero
    print("Pila vacía")

# Ejercicio

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


#############################
# Seccion 6: Clases en python
#############################

# Introducción a las clases
mensaje = "Hola mundo"
type(mensaje)

# Clase: es el plano de construcción
# Objeto: es una instancia de una clase

# Creando clases (PascalCase o UpperCamelCase)
# Así cuendo instancie no pongo como en otros lenguajes


class Perro:
    def habla(self):  # Esto ya no se llama función, es un método. Self es obligatorio
        print("Guay!")


mi_perro = Perro()  # Esto es como new Perro() en otros leguajes
type(mi_perro)      # Vemos a que clase pertenee
mi_perro.habla()    # No le paso ningún argumento
# Preguntamos si mi_perro es una instancia de Perro
isinstance(mi_perro, Perro)

# Constructor
# Es un método que se ejecuta siempre que se cree una instancia de la clase.


class Perro:
    # self hace referencia a la instancia creada, es decir "mi_perro"
    def __init__(self, nombre, edad):
        self.nombre = nombre    # Creación de ATRIBUTOS o PROPIEDAD
        self.edad = edad

    def habla(self):  # Esto ya no se llama función, es un método. Self es obligatorio
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Toby", 23)
print(mi_perro.nombre)

mi_perro2 = Perro("Felipe", 1)
print(mi_perro2.nombre)


# Propiedades de las clases
# Diferencia entre propiedades de clase y de instancia


class Perro:
    patas = 4  # Propiedad de la clase
    # self hace referencia a la instancia creada, es decir "mi_perro"

    def __init__(self, nombre, edad):
        self.nombre = nombre    # Creación PROPIEDAD de instancias (atributos)
        self.edad = edad        # Creación PROPIEDAD de instancias (atributos)

    def habla(self):  # Esto ya no se llama función, es un método. Self es obligatorio
        print(f"{self.nombre} dice: Guau!")


mi_perro = Perro("Toby", 3)
print(Perro.patas)  # => 4 Puedo acceder a través de la clase
print(mi_perro.patas)  # => 4
Perro.patas = 5
print(Perro.patas)  # => 5
print(mi_perro.patas)  # => 5
mi_perro.patas = 6
print(Perro.patas)  # => 5
print(mi_perro.patas)  # => 6
Perro.patas = 7
mi_perro2 = Perro("Jango", 5)
print(Perro.patas)  # => 7
print(mi_perro2.patas)  # => 7
print(mi_perro.patas)  # => 6 YA NO ES 7 PORQUE LO MODIFIQUE UNA VEZ


# Método de clase
# Usos:
# 1) Métodos en común para todas las intancias de la clase
# 2) Factory method para crear intancias de la clsae

class Perro:
    patas = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def habla(cls):  # cls se refiere a la clase misma: Perro
        print("Guau!")

    @classmethod
    def factory(cls):  # Factory method. Crea instancias de perro
        return cls("Toby", 4)


perro3 = Perro.factory()


# Propiedades y métodos privados

class Perro:

    def __init__(self, nombre, edad):
        self.__nombre = nombre  # Propiedades privadas
        self.edad = edad

    def get_nombre(self):
        return self.__nombre

    # Encapsular la asignación de nombre en un método puede servir
    # para aplicar cierta lógica de negocio y evitar que se
    # asignen, por ejemplo un número negativo al nombre del perro
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def __habla(self):  # MÉTODO PRIVADO
        print(f"{self.__nombre} dice: Guau!")

    @classmethod
    def factory(cls):  # Factory method. Crea instancias de perro
        return cls("Toby", 4)


perro1 = Perro.factory()
print(perro1.habla())
print(perro1.__nombre)  # => error, atributo privado
print(perro1.get_nombre())

# Puedo hackear y ver las propiedades privadas de todas formas
# Pero no hay que hacerlo ya que si se ha declarado privado
# es porque el desarrollador lo ha estipulado así.
print(perro1.__dict__)
print(perro1._Perro__nombre)

# Decorador property

class Perro:

    def __init__(self, nombre, edad):
        self.nombre = nombre #Pasa por la validación del setter

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nombre):
        if nombre.strip()
            self.__nombre = nombre
        return

perro = Perro("Toby")

# Métodos mágicos
# Se ejecuntan cuando no lo llamamos directamente
# __init__ es uno de ellos
# Todos comienzan y terminan con __
# Google: https://rszalski.github.io/magicmethods/ Representing your classes
# 
class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre   
        self.edad = edad

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):  # Esto ya no se llama función, es un método. Self es obligatorio
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Toby")
text = str(perro) #=> Llama a nuestro método mágico __str__

# Destructor
# Es un método mágico

class Perro:
    def __init__(self, nombre, edad):
        self.nombre = nombre   
        self.edad = edad

    def __del__(self):
        print(f"Chao peror :-( {self.nombre}")

    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):  # Esto ya no se llama función, es un método. Self es obligatorio
        print(f"{self.nombre} dice: Guau!")


perro = Perro("Toby")
del perro

# Comparación de objetos

class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro): #Otra instancia de la otra clase
        return self.lat == otro.lat and self.lon == otro.lon
    # Python es capaz de inferir el métod mágico __ne__ si ya tengo el __eq__
    
    
    # Con lo cual no es necesario ponerlo
    def __ne__(self, otro):
        return self.lat != otro.lat or self.lon != otro.lon
    # Python es capaz de inferir el métod mágico __ne__ si ya tengo el __eq__
    
    def __lt__(self, otro): # less than: coords < coords2) 
        return self.lat + self.lon < otro.lat + otro.lon
    # Python infiere automáticamente el coords > coords2

    def __le__(self, otro): #less or equal
        return self.lat + self.lon <= otro.lat + otro.lon
    # Python infiere automáticamente el coords >= coords2

    
coords = Coordenadas(45,27)
coords2 = Coordenadas(45, 27)
print(coords == coords2) # Sin método mágico __eq__
#=> False porque ocupan dos espacios en memoria diferentes. No son el mismo objeto
print(coords == coords2) # Con método mágico __eq__
# Cuando defino el método mágico __eq__, la cosa cambia

print(coords != coords2) # Con método mágico __eq__

print(coords < coords2) # Con método mágico __lt__

print(coords <= coords2) # Con método mágico __le__

# Contenedores: Meter objetos dentro de otros objetos

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def __str__(self):
        return f"Producto {self.nombre} - Precio: {self.precio}"
        
    


class Categoria:
    productos = []
    def __init__(self, nombre, productos):
        self.nombre = nombre
        self.productos = productos
    
    def agregar(self, producto):
        self.productos.append(producto)

    def imprimir(self):
        for producto in self.productos:
            print(producto)

kayak = Producto("Kayak", 1000)
bicicleta = Producto("Bicicleta", 750)
surfboard = Producto("Surfboard", 500)
deportes = Categoria("Deporte", [kayak, bicicleta])

deportes.agregar(surfboard)

deportes.imprimir()


# Herencia
class Animal:
    def comer(self):
        print("comieno")

    
class Perro(Animal):
    def pasear(self):
        print("paseando")

perro = Perro()

class Chanchito(Perro): #Herencia multinivel. No hacerlo con más de 1 o 2 niveles
    
    def programar(self):
        print("programando")

# Herencia múltiple

class Animal:
    def comer(self):
        print("comieno")
    
    def pasear(self):
        print("paseando animales")

    
class Perro():
    def pasear(self):
        print("paseando al perro")


# Cuidado con el orden de herencia, del orden depende los métodos que se elijan
# en el caso de que estén repetidos. Se va de derecha a izquierda, quedándose con el 
# de más a la izquierda.
class Chanchito(Perro, Animal):
    
    def programar(self):
        print("programando")

chanchito = Chanchito()
chanchito.pasear() #=> "paseando al perro".
# Recoge los métodos de izquierda a derecha en función del orden
# en cómo se ha definido la herencia. Chanchito(Perro, Animal)
# Si la hubiera definido Chanchito(Animal, Perro) imprimiría
# "paseando animal"