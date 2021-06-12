import numpy as np

def resolverSistemaLinearTriangularInferior(A, b):
    n = len(A)
    x = np.zeros(n)

    for i in range(0, n): # 0 até n-1
        soma = 0.0
        for j in range(0, i): # 0 até i-1
            soma = soma + A[i, j] * x[j]
        x[i] = (b[i] - soma)/A[i, i]
    return x

A = np.array(
    [
            [3.0,   0.0,    0.0],
            [1.0,   2.0,    0.0],
            [2.0,   -4.0,   1.0],
    ]
)
b = np.array(
    [9.0,   5.0,    7.0]
)

x = resolverSistemaLinearTriangularInferior(A, b)
print(x)
# solução : x = [3.0, 1.0, 5.0]

