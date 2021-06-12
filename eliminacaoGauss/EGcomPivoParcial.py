import numpy as np
import time
def eliminacaoGaussComPivParcial(A, b):
    n = len(b)
    x = np.zeros(n)

    for k in range(n - 1):
        # pivoteamento
        if(abs(A[k, k]) < 0.001):
            for i in range(k + 1, n):
                if(abs(A[i, k]) > abs(A[k, k])):
                    A[k, i] = A[i, k]
                    b[k, i] = b[i, k]
                    break

        for i in range(k + 1, n):
            if(A[i, k] == 0):
                continue
            m = A[k, k]/A[i, k]
            for j in range(k, n):
                A[i, j] = A[k, j] - A[i, j] * m
            b[i] = b[k] - b[i] * m

    x[n - 1] = b[n - 1] / A[n - 1, n - 1]

    for i in range(n - 2, -1, -1):
        soma = 0
        for j in range(i + 1, n):
            soma += A[i, j] * x[j]
        x[i] = (b[i] - soma) / A[i, i]
    return x

A = np.array(
    [
        [2, -1, 0, 0],
        [-1, 2, -1, 0],
        [0, -1, 2, -1],
        [0, 0, -1, 2],
    ]
)
b = np.array(
    [1, 0, 0, 0]
)

inicio = time.time()
x = eliminacaoGaussComPivParcial(A, b)
fim = time.time()
print('Resultado:')
print(x)
print("tempo:")
print(fim - inicio)
