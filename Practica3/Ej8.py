class Persona:
    def __init__(self, nombre, edad, ciudad):
        self.nombre = nombre
        self.edad = edad
        self.ciudad = ciudad

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ciudad: {self.ciudad}"

# Obtener datos desde el teclado
nombre = input("Ingrese el nombre: ")
edad = input("Ingrese la edad: ")
ciudad = input("Ingrese la ciudad: ")

# Crear una instancia de la clase Persona con los datos ingresados
persona = Persona(nombre, edad, ciudad)

# Imprimir los datos de la persona
print("Datos de la persona:")
print(persona)
