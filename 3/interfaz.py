import tkinter as tk
from tkinter import messagebox
from main import Escuela

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Aprobados y Reprobados")
        self.root.geometry("500x400")  # Ajuste del tamaño de la ventana

        # Instancia de la clase Escuela
        self.escuela = Escuela()

        # Widgets mejorados
        self.lbl_nombre = tk.Label(root, text="Nombre del alumno:", font=('Arial', 12))
        self.lbl_nombre.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        self.entry_nombre = tk.Entry(root, font=('Arial', 12), width=20)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.lbl_calificacion = tk.Label(root, text="Calificación del alumno:", font=('Arial', 12))
        self.lbl_calificacion.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        self.entry_calificacion = tk.Entry(root, font=('Arial', 12), width=20)
        self.entry_calificacion.grid(row=1, column=1, padx=10, pady=10)

        # Botón para agregar alumno
        self.btn_agregar = tk.Button(root, text="Agregar Alumno", command=self.agregar_alumno, font=('Arial', 10), bg="green", fg="white", width=20)
        self.btn_agregar.grid(row=2, column=0, columnspan=2, pady=10)

        # Alumnos Aprobados
        self.lbl_aprobados = tk.Label(root, text="Alumnos Aprobados:", font=('Arial', 12))
        self.lbl_aprobados.grid(row=3, column=0, padx=10, pady=10, sticky="w")

        self.lista_aprobados = tk.Listbox(root, font=('Arial', 10), width=25, height=10)
        self.lista_aprobados.grid(row=4, column=0, padx=10, pady=10)

        # Alumnos Reprobados
        self.lbl_reprobados = tk.Label(root, text="Alumnos Reprobados:", font=('Arial', 12))
        self.lbl_reprobados.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        self.lista_reprobados = tk.Listbox(root, font=('Arial', 10), width=25, height=10)
        self.lista_reprobados.grid(row=4, column=1, padx=10, pady=10)

    def agregar_alumno(self):
        nombre = self.entry_nombre.get()
        calificacion = self.entry_calificacion.get()
        if nombre and calificacion.isdigit():
            calificacion = int(calificacion)
            self.escuela.agregar_alumno(nombre, calificacion)

            # Limpiar listas visuales
            self.lista_aprobados.delete(0, tk.END)
            self.lista_reprobados.delete(0, tk.END)

            # Mostrar alumnos aprobados y reprobados
            for alumno in self.escuela.aprobados:
                self.lista_aprobados.insert(tk.END, str(alumno))

            for alumno in self.escuela.reprobados:
                self.lista_reprobados.insert(tk.END, str(alumno))

            # Limpiar las entradas de texto
            self.entry_nombre.delete(0, tk.END)
            self.entry_calificacion.delete(0, tk.END)
        else:
            messagebox.showerror("Error", "Por favor, ingrese un nombre y una calificación válida.")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
