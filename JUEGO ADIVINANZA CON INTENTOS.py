import random

# Paso 1: Escribir la primera prueba
import pytest

def test_generar_numero_secreto():
    minimo = 1
    maximo = 100
    numero_secreto = generar_numero_secreto(minimo, maximo)
    assert minimo <= numero_secreto <= maximo

# Paso 2: Escribir el código mínimo para que la prueba pase
def generar_numero_secreto(minimo, maximo):
    return random.randint(minimo, maximo)

# Paso 3: Escribir pruebas adicionales
def test_verificar_suposicion_demasiado_alta():
    numero_secreto = 50
    suposicion = 75
    resultado = verificar_suposicion(numero_secreto, suposicion)
    assert resultado == "Demasiado alto"

def test_verificar_suposicion_demasiado_baja():
    numero_secreto = 50
    suposicion = 25
    resultado = verificar_suposicion(numero_secreto, suposicion)
    assert resultado == "Demasiado bajo"

def test_verificar_suposicion_correcta():
    numero_secreto = 50
    suposicion = 50
    resultado = verificar_suposicion(numero_secreto, suposicion)
    assert resultado == "Has ganado!"

# Paso 4: Desarrollar el código para que las pruebas pasen
def verificar_suposicion(numero_secreto, suposicion):
    if suposicion < numero_secreto:
        return "Demasiado bajo"
    elif suposicion > numero_secreto:
        return "Demasiado alto"
    else:
        return "Has ganado!"

# Ejecutar las pruebas si se ejecuta este archivo como un script
if __name__ == "__main__":
    pytest.main([__file__])
