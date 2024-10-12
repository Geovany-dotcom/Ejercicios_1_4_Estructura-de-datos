class Producto:
    def __init__(self, clave, nombre, precio):
        self.clave = clave
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"Clave: {self.clave}, Nombre: {self.nombre}, Precio: ${self.precio:.2f}"

class Tienda:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, clave, nombre, precio):
        producto = Producto(clave, nombre, precio)
        self.productos.append(producto)

    def eliminar_producto(self, clave):
        self.productos = [producto for producto in self.productos if producto.clave != clave]

    def ordenar_productos(self):
        self.productos.sort(key=lambda producto: producto.nombre)

    def calcular_total(self):
        return sum(producto.precio for producto in self.productos)
