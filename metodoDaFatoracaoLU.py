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

def imprimirMatriz(M):
    n = len(M)
    for i in range(0, n):
        for j in range(0, n):
            print("%.3f\t" %M[i][j], end="")
        print("")

# Fase de decomposição
# Retorna a matriz [L\U]
# A = LU

# L =   [1          0       0]
#       [L[1][0]    1       0]
#       [L[2][0]    L[2][1] 1]

# U =   [U[0][0]    U[0][1]     U[0][2] ]
#       [0          U[1][1]     U[1][2] ]
#       [0          0           U[2][2] ]

#   [L\U] = [U[0][0]    U[0][1]     U[0][2] ]
#           [L[1][0]    U[1][1]     U[1][2] ]
#           [L[2][0]    L[2][1]     U[2][2] ]
def fatoracaoLU(A):
    n = len(A)
    for k in range(0, n - 1):
        for i in range(k + 1, n):
            if(A[i, k] != 0.0):
                '''
                    m: multiplicador para realizar a eliminação, 
                    que é armazenado na parte triangular inferior de A
                '''
                m = A[i, k] / A[k, k]
                # A[0, 0:3]: vetor das 3 colunas referente ao elemento A[0][0]
                A[i, (k + 1):n] = A[i, (k + 1):n] - m * A[k, (k + 1):n]
                A[i, k] = m
    return A

# O conteúdo de b é substituído por y durante a substituição direta
# Da mesma forma, a substituição posterior substitui y pela solução x.
def resolverLU(A, b):
    n = len(A)
    for k in range(1, n):
        # np.dot: retorna o produto escalar de A[k, 0:k] e b[0:k]
        b[k] = b[k] - np.dot(A[k, 0:k], b[0:k])

    b[n - 1] = b[n - 1] / A[n - 1, n - 1]

    for k in range(n-2, -1, -1):
        b[k] = (b[k] - np.dot(A[k, (k + 1):n], b[(k + 1):n])) / (A[k, k])

    return b

# Exemplo 7
A = np.array(
    [
        [4,     -1,     0,      -1,     0,      0],
        [-1,    4,      -1,     0,      -1,     0],
        [0,     -1,     4,      0,      0,      -1],
        [-1,    0,      0,      4,      -1,     0],
        [0,     -1,     0,      -1,     4,      -1],
        [0,     0,      -1,     0,      -1,     4]
    ]
)
b = np.array(
    [9.0, 3.0, -2.0, 1, 1, 1]
)
Ap = fatoracaoLU(A)
# print("fatoracaoLU")
# imprimirMatriz(Ap)
x = resolverLU(Ap, b)

# x = A^-1 * b
# A^-1 = x * b^-1

print("resolverLU")
for i in range(0, len(x)):
    print("%.3f\t" %x[i], end="")




