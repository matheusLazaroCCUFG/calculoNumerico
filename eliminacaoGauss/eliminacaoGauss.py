import time
import numpy as np

def eliminacaoGauss(A, b):
    n = len(A)
    # Eliminacao:
    for k in range(0, n-1):
        for i in range(k+1, n):
            m = A[i, k] / A[k, k]
            A[i, k] = 0.0
            for j in range(k+1, n):
                A[i, j] = A[i, j] - m * A[k, j]
            b[i] = b[i] - m * b[k]
    # Resolução do sistema triangular superior
    x = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0])

    x[n-1] = b[n-1] / A[n-1, n-1]
    for i in range(n-2, -1, -1):
        soma = 0
        for j in range(i+1, n):
            soma = soma + A[i, j] * x[j]
        x[i] = (b[i] - soma)/A[i, i]
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
x = eliminacaoGauss(A, b)
fim = time.time()
print("solucao:")
for i in range(len(b)):
    print("%.3f\t" %x[i], end="")

print("Tempo de execuçao: ")
print("%.10f\n" %(fim - inicio))