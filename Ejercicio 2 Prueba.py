from random import randint

# INGRESO Y VALIDACIÓN RANGO
while True:

    try:
        num1 = int(input("Ingrese límite inferior: "))
        num2 = int(input("Ingrese límite superior: "))

        if num1 < num2:
            break
        else:
            print("Error: el límite inferior debe ser menor que el superior.")

    except:
        print("Debe ingresar solo números enteros.")

# GENERAR NÚMERO ALEATORIO
numero = randint(num1, num2)

# Ajustar para que sea par
if numero % 2 != 0:

    if numero + 1 <= num2:
        numero = numero + 1
    else:
        numero = numero - 1

# INTENTO 1
while True:

    try:
        intento1 = int(input("Intente adivinar: "))
        break

    except:
        print("Debe ingresar un número entero.")

if intento1 == numero:
    print("Felicitaciones, adivinó en el primer intento.")

else:

    if intento1 < numero:
        print("El número es mayor.")
    else:
        print("El número es menor.")

    # INTENTO 2
    while True:

        try:
            intento2 = int(input("Intente de nuevo: "))
            break

        except:
            print("Debe ingresar un número entero.")

    if intento2 == numero:
        print("Felicitaciones, adivinó en su segundo intento.")

    else:

        if intento2 < numero:
            print("El número es mayor.")
        else:
            print("El número es menor.")

        # PISTA
        distancia1 = abs(numero - intento1)
        distancia2 = abs(numero - intento2)

        print("Te daré una pista:")

        if distancia1 < distancia2:
            print("El número que buscas está más cerca de", intento1, "que de", intento2)
        else:
            print("El número que buscas está más cerca de", intento2, "que de", intento1)

        # INTENTO 3
        while True:

            try:
                intento3 = int(input("Intente la última vez: "))
                break

            except:
                print("Debe ingresar un número entero.")

        if intento3 == numero:
            print("Felicitaciones, pudiste adivinar.")
        else:
            print("Perdiste.")
            print("El número era:", numero)