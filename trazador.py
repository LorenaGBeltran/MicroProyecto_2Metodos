import bisect
import numpy as np
import copy

def calc_tridiagonal(length, diff):
    A = np.zeros((length, length))
    A[0, 0] = 1.0
    for i in range(length - 1):
        if i != (length - 2):
            A[i + 1, i + 1] = 2.0 * (diff[i] + diff[i + 1])
        A[i + 1, i] = diff[i]
        A[i, i + 1] = diff[i]

    A[0, 1] = 0.0
    A[length - 1, length - 2] = 0.0
    A[length - 1, length - 1] = 1.0
    print(A)
    return A

def calc_resultados(length, res, diff):
    B = np.zeros(length)
    for i in range(length - 2):
        B[i + 1] = 3.0 * (res[i + 2] - res[i + 1]) / \
                diff[i + 1] - 3.0 * (res[i + 1] - res[i]) / diff[i]
    print(B)
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
        print(self.c)
        
temp=[0,8,16,24,32,40]
o=[14.621,11.843,9.870,8.418,7.305,6.413]
trazador = Trazador_cubico(temp[-4:], o[-4:])
