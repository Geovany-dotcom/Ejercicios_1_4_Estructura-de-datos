import tkinter as tk
from tkinter import messagebox
from main import Tienda

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestión de Productos")
        self.root.geometry("500x450")  # Ajuste del tamaño de la ventana

        # Instancia de la clase Tienda
        self.tienda = Tienda()

        # Etiquetas y campos de entrada mejorados
        self.lbl_clave = tk.Label(root, text="Clave del producto:", font=('Arial', 12))
        self.lbl_clave.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.entry_clave = tk.Entry(root, font=('Arial', 12), width=20)
        self.entry_clave.grid(row=0, column=1, padx=10, pady=10)

        self.lbl_nombre = tk.Label(root, text="Nombre del producto:", font=('Arial', 12))
        self.lbl_nombre.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.entry_nombre = tk.Entry(root, font=('Arial', 12), width=20)
        self.entry_nombre.grid(row=1, column=1, padx=10, pady=10)

        self.lbl_precio = tk.Label(root, text="Precio del producto:", font=('Arial', 12))
        self.lbl_precio.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.entry_precio = tk.Entry(root, font=('Arial', 12), width=20)
        self.entry_precio.grid(row=2, column=1, padx=10, pady=10)

        # Botones mejorados
        self.btn_agregar = tk.Button(root, text="Agregar Producto", command=self.agregar_producto, font=('Arial', 10), bg="green", fg="white", width=20)
        self.btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

        self.btn_eliminar = tk.Button(root, text="Eliminar Producto", command=self.eliminar_producto, font=('Arial', 10), bg="red", fg="white", width=20)
        self.btn_eliminar.grid(row=4, column=0, columnspan=2, pady=10)

        self.btn_ordenar = tk.Button(root, text="Ordenar Productos", command=self.ordenar_productos, font=('Arial', 10), bg="blue", fg="white", width=20)
        self.btn_ordenar.grid(row=5, column=0, columnspan=2, pady=10)

        self.btn_total = tk.Button(root, text="Mostrar Total", command=self.mostrar_total, font=('Arial', 10), bg="purple", fg="white", width=20)
        self.btn_total.grid(row=6, column=0, columnspan=2, pady=10)

        # Listbox para mostrar los productos
        self.lista_productos = tk.Listbox(root, font=('Arial', 10), width=45, height=10)
        self.lista_productos.grid(row=7, column=0, columnspan=2, padx=10, pady=10)

    def agregar_producto(self):
        clave = self.entry_clave.get()
        nombre = self.entry_nombre.get()
        precio = self.entry_precio.get()

        if clave and nombre and precio.replace('.', '', 1).isdigit():
            precio = float(precio)
            self.tienda.agregar_producto(clave, nombre, precio)
            self.actualizar_lista()
            self.entry_clave.delete(0, tk.END)
            self.entry_nombre.delete(0, tk.END)
            self.entry_precio.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, ingrese datos válidos para todos los campos.")

    def eliminar_producto(self):
        clave = self.entry_clave.get()
        if clave:
            self.tienda.eliminar_producto(clave)
            self.actualizar_lista()
            self.entry_clave.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, ingrese una clave de producto válida.")

    def ordenar_productos(self):
        self.tienda.ordenar_productos()
        self.actualizar_lista()

    def mostrar_total(self):
        total = self.tienda.calcular_total()
        messagebox.showinfo("Total", f"El costo total de los productos es: ${total:.2f}")

    def actualizar_lista(self):
        self.lista_productos.delete(0, tk.END)
        for producto in self.tienda.productos:
            self.lista_productos.insert(tk.END, str(producto))

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
