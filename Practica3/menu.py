
from operaciones import dividir

def mostrar_menu():
    print("1. Dividir dos números")
    print("2. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            num1 = float(input("Ingrese el primer número: "))
            num2 = float(input("Ingrese el segundo número: "))
            resultado = dividir(num1, num2)
            print(f"Resultado de la división: {resultado}")

        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()


# menu.py
from operaciones import dividir

def mostrar_menu():
    print("1. Dividir dos números")
    print("2. Salir")

def ejecutar_menu():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
                dividir(num1, num2)
            except ValueError:
                print("Error: Ingrese números válidos")

        elif opcion == "2":
            print("Saliendo del programa. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    ejecutar_menu()
