import random

def generar_numero_secreto(minimo, maximo):
    return random.randint(minimo, maximo)

def verificar_suposicion(numero_secreto, suposicion):
    if suposicion < numero_secreto:
        return "Demasiado bajo"
    elif suposicion > numero_secreto:
        return "Demasiado alto"
    else:
        return "Has ganado!"

def main():
    print("Bienvenido al Juego de Adivinanzas Hecho por Anyelo!")
    minimo = int(input("Ingrese el número mínimo del rango: "))
    maximo = int(input("Ingrese el número máximo del rango: "))
    
    numero_secreto = generar_numero_secreto(minimo, maximo)
    intentos_maximos = 5
    intentos_realizados = 0

    print(f"¡Adivina el número secreto entre {minimo} y {maximo}!")

    while intentos_realizados < intentos_maximos:
        suposicion = int(input("Ingresa tu suposición: "))
        intentos_realizados += 1
        resultado = verificar_suposicion(numero_secreto, suposicion)
        print(resultado)

        if resultado == "Has ganado!":
            print(f"Felicidades! Has adivinado el número en {intentos_realizados} intentos.")
            break

    if resultado != "Has ganado!":
        print(f"Lo siento, has agotado tus {intentos_maximos} intentos. El número secreto era {numero_secreto}.")

if __name__ == "__main__":
    main()
