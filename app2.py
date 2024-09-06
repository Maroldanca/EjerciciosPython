import random

#WHILE Y COLECCIONES

#Ejercicio 1

def eliminar_duplicados(lista):

    conjunto_unico = set(lista)

    lista_sin_duplicados = list(conjunto_unico)

    return lista_sin_duplicados

lista_con_duplicados = [1, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 9, 9, 9, 1]
resultadoWhile = eliminar_duplicados(lista_con_duplicados)
print(resultadoWhile)

#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 2

def juego_aleatorio():

    numero_secreto = random.randint(1, 100)
    intentos_maximos = 7
    intentos_restantes = intentos_maximos

    print("He pensado en un numero del 1 al 100")
    print(f"tienes {intentos_maximos} intentos para adivinar el numero")

    while intentos_restantes > 0:
        try:
            adivinanza = int(input("Introduce tu adivinanza: "))

        except ValueError:
            print("Por favor, ingresa un numero valido")
            continue

    if adivinanza == numero_secreto:
         print("¡Felicidades! Adivinaste el numero")
            

    elif adivinanza < numero_secreto:
        print("El numero es menor al numero secreto")

    else:
        print("El numero es mayor al numero secreto")

        intentos_restantes -= 1
        print(f"Te quedan {intentos_restantes} intentos para adivinar.")

    if intentos_restantes == 0:
        print(f"Lo siento, te quedaste sin mas intentos. El numero secreto es {numero_secreto}.")

juego_aleatorio()

#--------------------------------------------------------------------------------------------------------------------------------
#Ejercicio 3





