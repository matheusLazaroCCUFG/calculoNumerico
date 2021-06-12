import numpy as np
import math

def metodoCholesky(matriz):
    n = len(matriz)
    L = np.zeros((n, n))

    for i in range(n):
        for j in range(i + 1):
            soma = 0
            if(j != i):
                for k in range(j):
                    soma = soma + (L[i, k] * L[j, k])
                if(L[j, j] > 0):
                    L[i, j] = int((matriz[i, j] - soma)/L[j, j])
            else:
                for k in range(j):
                    soma = soma + pow(L[j, k], 2)
                L[j, i] = int(math.sqrt(matriz[j, j] - soma))
    #print(L)
    return L

def resolveSistema(G, gTransposta, b):
    n = len(G)

    y = np.zeros(n)
    for i in range(n):  # laço de repetição decrescente de n-1 até 0
        soma = 0
        for j in range(i):
            soma = soma + G[i, j] * y[j]
        y[i] = (b[i] - soma) / G[i, i]

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i, n):
            soma = soma + gTransposta[i, j] * x[j]
        x[i] = (y[i] - soma) / gTransposta[i, i]

    return x

matriz = np.array(
    [
        [20,    7,      9 ],
        [7,     30,     8 ],
        [9,     8,      30]
    ]
)
b = np.array(
    [16, 38, 38]
)

L = metodoCholesky(matriz)

x = resolveSistema(L, np.transpose(L), b)
print(x)