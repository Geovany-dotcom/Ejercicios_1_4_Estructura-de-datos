import random

class Numeros:
    def __init__(self):
        self.numeros = []
        self.pares = []
        self.impares = []

    def generar_numeros(self, cantidad):
        """Genera una lista de números aleatorios"""
        self.numeros = [random.randint(1, 100) for _ in range(cantidad)]

    def separar_pares_impares(self):
        """Separa los números pares e impares de la lista generada"""
        self.pares = [num for num in self.numeros if num % 2 == 0]
        self.impares = [num for num in self.numeros if num % 2 != 0]
