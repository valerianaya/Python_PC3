class Producto:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

    def __str__(self):
        # Separar el código en partes utilizando '-' como delimitador
        partes_codigo = self.codigo.split('-')

        # Obtener las partes individuales del código
        pais = partes_codigo[0]
        lote = partes_codigo[1]
        anio = partes_codigo[2]

        return f"Nombre: {self.nombre}, Código: {self.codigo}\nPaís: {pais}, Número de Lote: {lote}, Año: {anio}"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear un objeto Producto
    producto_ejemplo = Producto("Ejemplo", "PERU-0001-2023")

    # Imprimir el objeto de forma literal
    print(producto_ejemplo)
