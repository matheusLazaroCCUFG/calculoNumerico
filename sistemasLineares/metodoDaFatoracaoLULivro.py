'''
Universidade Federal de Goiás
abril de 2021
Aluno: Matheus Lázaro Honório da Silva
Disciplina: Cálculo Numérico
    Fatoração LU
        * É possível mostrar que qualquer matriz quadrada A
        pode ser expressa como um produto de uma matriz triangular
        inferior L e uma matriz triangular superior U.
        * A = LU
        * O processo de calcular L e U para um determinado A
        é conhecido como decomposição LU ou fatoração LU.
        * Após decompor A, é fácil resolver as equações Ax = b.
        Primeiro reescrevemos as equações como LUx = b, depois
        de usar a notação Ux = y, as equações tornam-se:
        * Ly = b
        * que pode ser resolvido para y por substituição direta.
        * Então, Ux = y.
        * Isso irá render pelo processo de substituição de volta.
        * A vantagem da decomposição LU sobre o método da eliminação
        de Gauss é que uma vez que A é decomposta, podemos resolver
        Ax = b para tantos vetores constantes b quanto quisermos.
        * O custo de cada solução adicional é relativamente pequeno,
        porque as operações de substituição direta e reversa consomem
        muito menos tempo do que o processo de decomposição.
'''
import numpy as np

def imprimirMatriz(A):
    n = len(A)
    for i in range(n):
        for j in range(n):
            print("%.3f\t" %A[i][j], end="")
        print("")
    print("")
# Ax = b, A: n x n
# p: permutações realizadas durante a fatoração
def fatoracaoLUcomPivotamentoParcial(A, b):
    n = len(A)
    cofator = np.zeros(n)
    L = np.zeros(n)
    U = np.zeros(n)
    # cálculo dos cofatores: para realizar a permutação
    for i in range(0, n):
        cofator[i] = i
    # print("cofatores: ")
    # print(cofator)

    print("A")
    imprimirMatriz(A)
    for k in range(0, n - 1): # 0 até n-2 no array
        pivo = abs(A[k, k])
        r = k
        for i in range(k, n): # k até n-1 no array
            if(abs(A[i, k]) > pivo):
                # maior elemento da coluna k (indice da referente iteração geral) da matriz A
                pivo = abs(A[i, k])
                r = i # r assume o índice da linha do maior elemento encontrado

        if(pivo == 0):
            # matriz A é singular, ou seja, possui determinante nulo (não admite inversa)
            # Obs.: Estamos calculando sistemas com solução única
            print("A matriz é singular. O sistema não admite uma única solução.")
            break # paramos a execução

        if(r != k):
            # Se o índice da linha do maior elemento de A na coluna k
            # for diferente de k
            # Aqui evitamos a realização de trocas desnecessárias.

            # troca entre os cofatores referentes
            aux = cofator[k]
            cofator[k] = cofator[r]
            cofator[r] = aux

            # trocamos as linhas r e j de A, passando
            # por todos os elementos da referentes colunas com j
            for j in range(0, n):
                aux = A[k, j]
                A[k, j] = A[r, j]
                A[r, j] = aux

        # Realização da eliminação e montagem de LU
        for i in range(k+1, n):
            # m: multiplicador para realizar a eliminação
            # que é armazenado na parte triangular inferior de A
            m = A[i, k] / A[k, k]
            A[i, k] = m
            for j in range(k+1, n):
                A[i, j] = A[i, j] - m * A[k, j]

        # Montagem do L e do U, a partir de A,
        # que assume o formato [L\U]:
        # Matriz triangular Superior U
        # com matriz triangular inferior L com 1's na diagonal principal
        #   [L\U] = [U[0,0]    U[0,1]     U[0,2] ]
        #           [L[1,0]    U[1,1]     U[1,2] ]
        #           [L[2,0]    L[2,1]     U[2,2] ]

        # L =   [1          0       0]
        #       [L[1,0]     1       0]
        #       [L[2,0]     L[2,1]  1]

        # U =   [U[0,0]     U[0,1]      U[0,2] ]
        #       [0          U[1,1]      U[1,2] ]
        #       [0          0           U[2,2] ]
        L = np.eye(n)
        U = np.zeros((n, n))
        for i in range(n):
            for j in range(n):
                if(i > j):
                    L[i, j] = A[i, j]
                elif(j >= i):
                    U[i, j] = A[i, j]

    print("L")
    imprimirMatriz(L)
    print("U")
    imprimirMatriz(U)

    #resolução dos sistemas triangulares
    c = np.zeros(n)
    # Cálculo do vetor c, utilizado para calcular o y
    for i in range(0, n):
        r = int(cofator[i])
        c[i] = b[r]
    # print("c:")
    # print(c)

    # Cálculo do vetor y, utilizado para calcular o vetor final x.
    y = np.zeros(n)
    for i in range(0, n):
        soma = 0
        for j in range(0, i):
            soma = soma + A[i, j] * y[j]
        y[i] = c[i] - soma
    print("Y")
    print(y)

    # Cálculo de vetor x, que é solução do sistema
    x = np.zeros(n)
    for i in range(n - 1, -1, -1): # laço de repetição decrescente de n-1 até 0
        soma = 0
        for j in range(i, n):
            soma = soma + A[i, j] * x[j]
        x[i] = (y[i] - soma) / A[i, i]

    print("Resultado: ")
    # print(x)
    for i in range(n):
        print("%.3f\t" %x[i], end="")

A = np.array(
    [
        [3.0, -4.0, 1.0],
        [1.0, 2.0, 2.0],
        [4.0, 0.0, -3.0]
    ]
)
b = np.array(
    [9.0, 3.0, -2.0]
)
print("Exemplo 7 do livro: ")
fatoracaoLUcomPivotamentoParcial(A, b)


print("\n---------------------------------------------------------------------")


A = np.array(
    [
        [4.0,   2.0,    1.0,    -2.0],
        [3.0,   -3.0,   -1.0,   -1.0],
        [3.0,   5.0,    1.0,    1.0],
        [1.0,   -1.0,   -1.0,   4.0]
    ]
)
b = np.array(
        [3.0,   2.0,    0.0,    -2.0]
)
print("Exemplo em sistema de 4 variáveis: ")
print("4x + 2y + z - 2t = 3")
print("3x - 3y - z - t = 2")
print("3x + 5y + z + t = 0")
print("x - y - z + 4t = -2")

fatoracaoLUcomPivotamentoParcial(A, b)


