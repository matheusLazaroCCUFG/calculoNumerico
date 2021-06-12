import time
import numpy as np

def eliminacaoGaussPivotamentoParcial(A, b):
    n = len(b)
    for k in range(0, n - 1):

        # Pivoteamento
        pivo = A[k, k]
        lPivo = k
        for i in range(k + 1, n - 1):
            if (abs(A[i, k]) > abs(pivo)):
                pivo = A[i, k]
                lPivo = i
        if pivo == 0:
            print("A matriz A é singular")
            break

        if lPivo != k:
            for j in range(0, n):
                troca = A[k, j]
                A[k, j] = A[lPivo, j]
                A[lPivo, j] = troca
            troca = b[k]
            b[k] = b[lPivo]
            b[lPivo] = troca

        # Eliminacao
        for i in range(k + 1, n):
            m = A[i, k] / A[k, k]
            A[i, k] = 0
            for j in range(k + 1, n):
                A[i, j] = A[i, j] - m * A[k, j]
            b[i] = b[i] - m * b[k]

    x = np.zeros(n)
    x[n - 1] = b[n - 1] / A[n - 1, n - 1]

    for i in range(n - 2, -1, -1):
        soma = 0
        for j in range(i, n):
            soma = soma + A[i, j] * x[j]
        x[i] = (b[i] - soma) / A[i, i]

    return x

A = np.array(
    [ # 2 <= i <= 9
        [2,  -1,   0,  0],
        [-1,  2,  -1,  0], # i = 2
        [0,  -1,   2, -1], # i = 3
        [0,   0,  -1,  2],
    ]
)
b = np.array(
    [1, 0, 0, 0]
)
inicio = time.time()
x = eliminacaoGaussPivotamentoParcial(A, b)
fim = time.time()
print("solucao:")
for i in range(len(b)):
    print("%.3f\t" %x[i], end="")
print("Tempo: ")
print("%.10f\n" %(fim - inicio))