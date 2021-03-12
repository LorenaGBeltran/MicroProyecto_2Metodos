import numpy as np
from trazador import *
import matplotlib.pyplot as plt
class Trazador2D:
    def __init__(self, x, y):
        self.s = self.trayectoria_s(np.diff(x), np.diff(y)) # suma acumulativa de distancia euclidiana entre puntos
        self.sx = Trazador_cubico(self.s, x) # paramétrica de x
        self.sy = Trazador_cubico(self.s, y) # paramétrica de y

    # dx y dy son las diff de x y de y
    def trayectoria_s(self, dx, dy):
        self.ds = [(idx ** 2 + idy ** 2)**0.5
                   for (idx, idy) in zip(dx, dy)] # Parametrizado
        s = [0.0]
        s.extend(np.cumsum(self.ds)) # Suma acumulativa
        return s

    # Devuelve las coordenadas de (s_x(t), s_y(t))
    def _calc(self, t):
        return self.sx.calc(t), self.sy.calc(t)

# Calculamos la curva de trayectoria con interpolación
# num es el número de puntos que queremos trazar
def interpolar_trazador_2d(x, y, num=100):
    tc = Trazador2D(x, y)
    s = np.linspace(0, tc.s[-1], num+1)[:-1] #longitud de la trayectoria
    s_x, s_y = [], []
    for i_s in s:
        interp = tc._calc(i_s)
        s_x.append(interp[0])
        s_y.append(interp[1])
    
    return s_x, s_y


def test2d(doPlot):
    # Una L que encontramos en Chegg
    prueba_y=[13.1,11,13,16,14.6,11,4.7,2.1,4.0,5.35,5.6,4.7,2.10,3.00]   
    prueba_x=[6.50,11,16,16.1,13.0,11,7.8,4.5,2.0,3.0,4.0,7.8,12.0,14.9]
    x, y = interpolar_trazador_2d(prueba_x, prueba_y, 250) #250 se acerca bastante al último punto
    if doPlot:    
        plt.plot(prueba_x, prueba_y, "xb")
        plt.plot(x, y, "r")
        plt.axis("equal")
        plt.xlabel("s(x)")
        plt.ylabel("s(y)")
        plt.show()

# test2d(True)
