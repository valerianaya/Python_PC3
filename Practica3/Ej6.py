# operaciones.py
import os

def dividir(numero1, numero2):
    try:
        resultado = numero1 / numero2
    except ZeroDivisionError:
        print("Error: No se puede dividir por cero")
    except Exception as e:
        print(f"Error inesperado: {e}")
    else:
        print(f"Resultado de la división: {resultado}")
    finally:
        print(f"Ruta del directorio de trabajo: {os.getcwd()}")
        print("Proceso terminado")
