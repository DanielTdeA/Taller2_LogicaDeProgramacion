numero = float(input("Ingrese un numero base: "))
exponente = int(input("Ingrese un exponente: "))

if exponente < 0:
    print("Los exponentes no puden ser negativos")
elif exponente == 0:
    resultado = 1
    print(f"El resultado es: {resultado}")
else:
    resultado = numero
    iteracion = 1
    while iteracion < exponente:
        resultado *= numero
        iteracion += 1
    print(f"El resultado es: {resultado}")
    
