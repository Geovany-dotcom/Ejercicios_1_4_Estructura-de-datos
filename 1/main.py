import random

class Producto:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cantidad = random.randint(1, 10)
        self.precio = random.uniform(5, 50)

    def __str__(self):
        return f"{self.nombre} - Cantidad: {self.cantidad}, Precio: ${self.precio:.2f}"

class Supermercado:
    def __init__(self):
        self.productos_disponibles = []
        self.productos_retirados = []

    def agregar_producto(self, nombre):
        producto = Producto(nombre)
        self.productos_disponibles.append(producto)
        return producto

    def retirar_producto(self, indice):
        if 0 <= indice < len(self.productos_disponibles):
            producto = self.productos_disponibles.pop(indice)
            self.productos_retirados.append(producto)
            return producto
        return None
