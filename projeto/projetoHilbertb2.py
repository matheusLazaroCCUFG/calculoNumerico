import numpy as np

def fatoracaoLUcomPivotamentoParcial(A, b):
    n = len(A)
    cofator = np.zeros(n)
    L = np.zeros(n)
    U = np.zeros(n)
    for i in range(0, n):
        cofator[i] = i


    for k in range(0, n - 1):
        pivo = abs(A[k, k])
        r = k
        for i in range(k, n):
            if(abs(A[i, k]) > pivo):
                pivo = abs(A[i, k])
                r = i

        if(pivo == 0):
            print("A matriz é singular. O sistema não admite uma única solução.")
            break

        if(r != k):
            aux = cofator[k]
            cofator[k] = cofator[r]
            cofator[r] = aux

            for j in range(0, n):
                aux = A[k, j]
                A[k, j] = A[r, j]
                A[r, j] = aux

        for i in range(k+1, n):
            m = A[i, k] / A[k, k]
            A[i, k] = m
            for j in range(k+1, n):
                A[i, j] = A[i, j] - m * A[k, j]

        L = np.eye(n)
        U = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if(i > j):
                    L[i, j] = A[i, j]
                elif(j >= i):
                    U[i, j] = A[i, j]

    c = np.zeros(n)
    for i in range(0, n):
        r = int(cofator[i])
        c[i] = b[r]

    y = np.zeros(n)
    for i in range(0, n):
        soma = 0
        for j in range(0, i):
            soma = soma + A[i, j] * y[j]
        y[i] = c[i] - soma

    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        soma = 0
        for j in range(i, n):
            soma = soma + A[i, j] * x[j]
        x[i] = (y[i] - soma) / A[i, i]

    print("Resultado: ")
    # print(x)
    for i in range(n):
        print("%.3f\t" %x[i], end="")

def matrizHilbert(n):
    H = np.zeros((n, n))
    for i in range(1, n+1):
        for j in range(1, n+1):
            H[i-1, j-1] = 1 / (i + j - 1)
    # print(H)
    return H

def formarBn(n):
    B = np.zeros(n+1)
    for i in range(1, n+1):
        soma = 0
        for j in range(1, n+1):
            soma += 1 / (i + j - 1)
            B[i-1] = soma
    # print(B)
    return B

for i in range(3, 50):
    print("n = ", i)
    A = matrizHilbert(i)
    b = formarBn(i)
    fatoracaoLUcomPivotamentoParcial(A, b)
    print("")

