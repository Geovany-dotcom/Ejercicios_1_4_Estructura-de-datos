import tkinter as tk
from tkinter import messagebox
from main import Supermercado

class SupermercadoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Supermercado - Gestión de Productos")
        self.root.geometry("500x400")  # Cambiar el tamaño de la ventana

        # Instancia de la clase Supermercado para la lógica del negocio
        self.supermercado = Supermercado()

        # Crear widgets con estilos mejorados
        self.lbl_nombre = tk.Label(root, text="Nombre del Producto:", font=('Arial', 12))
        self.lbl_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_nombre = tk.Entry(root, font=('Arial', 12), width=25)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        # Botones con mejor disposición
        self.btn_agregar = tk.Button(root, text="Agregar Producto", command=self.agregar_producto, font=('Arial', 10), bg="green", fg="white", width=15)
        self.btn_agregar.grid(row=1, column=0, padx=10, pady=10)

        self.btn_retirar = tk.Button(root, text="Retirar Producto", command=self.retirar_producto, font=('Arial', 10), bg="red", fg="white", width=15)
        self.btn_retirar.grid(row=1, column=1, padx=10, pady=10)

        # Labels y Listboxes mejor distribuidos y con tamaño ajustado
        self.lbl_disp = tk.Label(root, text="Productos Disponibles:", font=('Arial', 12))
        self.lbl_disp.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.lista_disp = tk.Listbox(root, font=('Arial', 10), width=30, height=10)
        self.lista_disp.grid(row=3, column=0, padx=10, pady=10)

        self.lbl_retirados = tk.Label(root, text="Productos Retirados:", font=('Arial', 12))
        self.lbl_retirados.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.lista_retirados = tk.Listbox(root, font=('Arial', 10), width=30, height=10)
        self.lista_retirados.grid(row=3, column=1, padx=10, pady=10)

    def agregar_producto(self):
        nombre = self.entry_nombre.get()
        if nombre:
            producto = self.supermercado.agregar_producto(nombre)
            self.lista_disp.insert(tk.END, str(producto))
            self.entry_nombre.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "Debe ingresar el nombre del producto")

    def retirar_producto(self):
        seleccion = self.lista_disp.curselection()
        if seleccion:
            producto = self.supermercado.retirar_producto(seleccion[0])
            if producto:
                self.lista_disp.delete(seleccion)
                self.lista_retirados.insert(tk.END, str(producto))
        else:
            messagebox.showwarning("Advertencia", "Debe seleccionar un producto para retirar")

if __name__ == "__main__":
    root = tk.Tk()
    app = SupermercadoApp(root)
    root.mainloop()
