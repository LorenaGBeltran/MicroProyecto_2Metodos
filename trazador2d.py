import numpy as np
from trazador import *
import matplotlib.pyplot as plt
class Trazador2D:
    def __init__(self, x, y):
        self.s = self.trayectoria_s(np.diff(x), np.diff(y)) # longitud acumulativa entre puntos
        self.sx = Trazador_cubico(self.s, x) # paramétrica de x
        self.sy = Trazador_cubico(self.s, y) # paramétrica de y

    # dx y dy son las diff de x y de y
    def trayectoria_s(self, dx, dy):
        self.ds = [(idx ** 2 + idy ** 2)**0.5
                   for (idx, idy) in zip(dx, dy)] # distancia euclidiana entre puntos
        s = [0.0]
        s.extend(np.cumsum(self.ds)) # Suma acumulativa de la longitud entre puntos
        return s


# Calculamos la curva de trayectoria con interpolación
# num es el número de puntos que queremos trazar
def interpolar_trazador_2d(x, y, num=100):
    tc = Trazador2D(x, y)
    s = np.linspace(0, tc.s[-1], num+1)[:-1] #longitud de la trayectoria
    s_x, s_y = [], []
    for i_s in s:
        s_x.append(tc.sx.calc(i_s))
        s_y.append(tc.sy.calc(i_s))
    
    return s_x, s_y
