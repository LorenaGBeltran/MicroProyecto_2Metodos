import numpy as np
import copy
import matplotlib.pyplot as plt

def calc_tridiagonal(length, diff):
    # diff = h_i
    A = np.zeros((length, length))
    A[0, 0] = 1.0
    for i in range(length - 1):
        if i != (length - 2):
            A[i + 1, i + 1] = 2.0 * (diff[i] + diff[i + 1]) # Diagonal de v_i
        # Adyacentes con h_i
        A[i + 1, i] = diff[i]
        A[i, i + 1] = diff[i]

    A[0, 1] = 0.0
    A[length - 1, length - 2] = 0.0
    A[length - 1, length - 1] = 1.0
    #print(A)
    return A

def calc_resultados(length, res, diff):
    B = np.zeros(length)
    for i in range(length - 2):
        # u_i
        B[i + 1] = 3.0 * (res[i + 2] - res[i + 1]) / \
                diff[i + 1] - 3.0 * (res[i + 1] - res[i]) / diff[i]
    #print(B)
    return B
    

class Trazador_cubico:
    def __init__(self, x, y):
        self.b, self.c, self.d = [], [], []

        # Como referencia para llamar en otras funciones
        # No se va a modificar
        self.x = x
        self.length = len(x)

        # Nuesta matriz de resultados
        # Hacemos copy para que no modifique el original
        self.res = copy.copy(y)

        # np.diff(x): Lista que contiene la diferencia entre el
        # i-ésimo y el i-ésimo - 1 elementos de x
        diff = np.diff(x)

        A = calc_tridiagonal(self.length, diff)
        B = calc_resultados(self.length, self.res, diff)
        self.c = np.matmul(np.linalg.inv(A),B)
        #print(self.c)

        # Encontramos b y d del trazador
        for i in range(self.length - 1):
            self.d.append((self.c[i + 1] - self.c[i]) / (3.0 * diff[i]))
            tb = (self.res[i + 1] - self.res[i]) / diff[i] - diff[i] * \
                 (self.c[i + 1] + 2.0 * self.c[i]) / 3.0
            self.b.append(tb)
        #print(self.b)
        #print(self.d)

    # Encuentra y(t); si t es más pequeño o mayor a los valores en x, return None
    def calc(self, t):

        if t < self.x[0]:
            return None
        elif t > self.x[-1]:
            return None

        i = [j - 1 for j in range(self.length) if self.x[j] - t > 0][0]
        dx = t - self.x[i]
        y = self.res[i] + self.b[i] * dx + self.c[i] * dx ** 2.0 + self.d[i] * dx ** 3.0
        return y

def test(doPlot):
    temp=[0,8,16,24,32,40]
    o=[14.621,11.843,9.870,8.418,7.305,6.413]
    trazador = Trazador_cubico(temp[-3:], o[-3:])
    print(trazador.calc(27), '\nValor real en el lab: 7.986\nValor obtenido con trazadores cúbicos usado en el lab: 8.043433400856753')
    if doPlot:
        plt.plot(temp[-3:], o[-3:], "xb")
        x = np.arange(temp[-3], temp[-1], 0.1) # 0.1 para que se vea bien pegado al último punto
        plt.plot(x, [trazador.calc(i) for i in x], "r")
        plt.axis("equal")
        plt.show()

# test(True)
