import numpy as np
import math


def gaussSeidel(A, b, iteracoes):
    iteracao = 0
    x = np.zeros(len(A))
    solucoes = np.zeros(len(A))
    while (iteracao < iteracoes):
        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if (i != j):
                    x -= A[i, j] * solucoes[j]
            x /= A[i, i]
            solucoes[i] = x
        iteracao += 1
    print("sol:")
    print(solucoes)



def criterioSassenfeld(A):
    coeficientes = np.zeros(len(A))

    for i in range(len(A)):
        b = 0
        for j in range(len(A)):
            if ((i != j and i == 0) or i < j):
                b = b + A[i, j]
            elif (i != j and i != 0):
                b = b + A[i, j] * coeficientes[j]
        b = b / A[i, i]
        np.append(coeficientes, b)  # anexar b ao fim
    maiorCoeficiente = max(coeficientes)
    if (maiorCoeficiente < 1):
        print("O método de Gauss-Seidel converge para o sistema")
    else:
        print("Não é possível afirmar a convergência do método de Gauss-Seidel no sistema")


A = np.array(
    [
        [5.0, 2.0],
        [1.0, 3.0],
    ]
)
b = np.array(
    [-3.0, 2.0]
)

print("solucao:")
gaussSeidel(A, b, 60)

criterioSassenfeld(A)
