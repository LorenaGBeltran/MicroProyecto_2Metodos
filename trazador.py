import bisect
import numpy as np
import copy

class Trazador_cubico:
    def __init__(self, x, y):
        self.b, self.c, self.d = [], [], []

        # Como referencia para llamar en otras funciones
        # No se va a modificar
        self.x = x

        # Nuesta matriz de resultados
        # Hacemos copy para que no modifique el original
        self.res = copy.copy(y)
