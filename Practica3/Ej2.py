import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        area = math.pi * self.radio**2
        return area

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un objeto Circulo con radio 6
    circulo_ejemplo = Circulo(6)

    # Calcular y mostrar el área del círculo
    area_calculada = circulo_ejemplo.calcular_area()
    print(f"Área del círculo con radio {circulo_ejemplo.radio}: {area_calculada}")
