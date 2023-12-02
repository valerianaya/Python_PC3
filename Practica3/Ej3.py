class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"{self.nombre} - ${self.precio:.2f}"

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_productos(self):
        print("Lista de productos:")
        for producto in self.productos:
            print(producto)

# Ejemplo de uso
if __name__ == "__main__":
    # Crear productos
    producto1 = Producto("Filtro de aceite", 15.99)
    producto2 = Producto("Batería para automóvil", 99.99)
    producto3 = Producto("Pastillas de freno", 24.50)

    # Crear un catálogo
    catalogo = Catalogo()

    # Agregar productos al catálogo
    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    # Mostrar la lista de productos en el catálogo
    catalogo.mostrar_productos()
