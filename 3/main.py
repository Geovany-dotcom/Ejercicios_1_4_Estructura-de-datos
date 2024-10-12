class Alumno:
    def __init__(self, nombre, calificacion):
        self.nombre = nombre
        self.calificacion = calificacion

    def __str__(self):
        return f"{self.nombre} - Calificación: {self.calificacion}"

class Escuela:
    def __init__(self):
        self.alumnos = []
        self.aprobados = []
        self.reprobados = []

    def agregar_alumno(self, nombre, calificacion):
        alumno = Alumno(nombre, calificacion)
        self.alumnos.append(alumno)
        if alumno.calificacion >= 7:
            self.aprobados.append(alumno)
        else:
            self.reprobados.append(alumno)
