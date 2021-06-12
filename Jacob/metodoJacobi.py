'''
Universidade Federal de Goiás
abril de 2021
Aluno: Matheus Lázaro Honório da Silva
Disciplina: Cálculo Numérico

    Método de Jacobi
        Transformar o sistema Linear Ax = b em x = Cx + g,
        sendo
            A[i, i] != 0
            i = 1, ..., n
        Isolar o vetor x mediante separação pela diagonal

'''
import numpy as np

def gaussJacobi(A, b, solucao, iteracoes):
    iteracao = 0
    vetAux = np.zeros(len(A))

    while(iteracao < iteracoes):
        for i in range(len(A)):
            x = b[i]
            for j in range(len(A)):
                if(i != j):
                    x = x - A[i, j] * solucao[j]
            x = x / A[i, i]
            vetAux[i] = x
        iteracao += 1

        for p in range(len(vetAux)):
            solucao[p] = vetAux[p]
    print(solucao)


A = np.array(
    [
        [5, 2],
        [1, 3]
    ]
)

b = np.array(
    [-3, 2]
)
x = np.zeros(len(A))
gaussJacobi(A, b, x, 60)