import tkinter as tk
from tkinter import messagebox
from main import Numeros

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Pares e Impares")
        self.root.geometry("500x350")  # Ajuste de tamaño de la ventana

        # Instancia de la clase Numeros para la lógica
        self.numeros_obj = Numeros()

        # Widgets mejorados
        self.lbl_cantidad = tk.Label(root, text="Cantidad de números a generar:", font=('Arial', 12))
        self.lbl_cantidad.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_cantidad = tk.Entry(root, font=('Arial', 12), width=15)
        self.entry_cantidad.grid(row=0, column=1, padx=10, pady=10)

        # Botón con estilo mejorado
        self.btn_generar = tk.Button(root, text="Generar y Separar", command=self.generar_separar, font=('Arial', 10), bg="blue", fg="white", width=20)
        self.btn_generar.grid(row=1, column=0, columnspan=2, pady=10)

        # Etiquetas y Listboxes para números pares e impares
        self.lbl_pares = tk.Label(root, text="Números Pares:", font=('Arial', 12))
        self.lbl_pares.grid(row=2, column=0, padx=10, pady=10, sticky="w")

        self.lista_pares = tk.Listbox(root, font=('Arial', 10), width=20, height=8)
        self.lista_pares.grid(row=3, column=0, padx=10, pady=10)

        self.lbl_impares = tk.Label(root, text="Números Impares:", font=('Arial', 12))
        self.lbl_impares.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.lista_impares = tk.Listbox(root, font=('Arial', 10), width=20, height=8)
        self.lista_impares.grid(row=3, column=1, padx=10, pady=10)

    def generar_separar(self):
        cantidad = self.entry_cantidad.get()
        if cantidad.isdigit():
            cantidad = int(cantidad)
            self.numeros_obj.generar_numeros(cantidad)
            self.numeros_obj.separar_pares_impares()

            # Limpiar las listas antes de mostrar nuevos valores
            self.lista_pares.delete(0, tk.END)
            self.lista_impares.delete(0, tk.END)

            # Mostrar los números pares e impares en sus respectivas listas
            for num in self.numeros_obj.pares:
                self.lista_pares.insert(tk.END, num)
            for num in self.numeros_obj.impares:
                self.lista_impares.insert(tk.END, num)
        else:
            messagebox.showerror("Error", "Por favor, ingrese un número válido.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
