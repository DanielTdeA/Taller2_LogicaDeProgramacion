import random

print("Hola, Bienvenido a adivina el numero, voy a generar un numero aleatorio ente 1 y 100 y debes tratar de adivinarlo.")
print("Si quieres rendirte solo debes colocar el numero 0.")
print("Comencemos!")

numero_aleatorio = random.randint(1,100)
numero_usuario = float(input("Ingresa un numero entre el 1 y el 100: "))

if numero_usuario == 0:
    print(f"Es una lastima que te rindas. Deshonra y desgracia para ti.")
else:
    while numero_aleatorio != numero_usuario:
        if numero_usuario == 0:
            print(f"Es una lastima que te rindas. Deshonra y desgracia para ti.")
            print(f"El numero que estabas buscando es el: {numero_aleatorio}")
            numero_usuario2 = numero_usuario 
            numero_usuario = numero_aleatorio #Para salir del bucle
        elif numero_usuario < numero_aleatorio:
            print(f"El numero que buscas es mayor a {numero_usuario}")
            numero_usuario = float(input("Ingresa un nuevo numero: "))
        elif numero_usuario > numero_aleatorio:
            print(f"El numero que buscas es menor a {numero_usuario}")
            numero_usuario = float(input("Ingresa un nuevo numero: "))
            
    if numero_usuario2 != 0:
        print(f"Muy bien! El numero que estabas buscando es el: {numero_aleatorio}")

    

