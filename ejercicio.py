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
