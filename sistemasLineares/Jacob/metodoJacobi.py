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

def verificarMatrizDiagonal(matriz):
    contador = 0
    for i in range(len(matriz)):
        soma = 0
        soma += sum(matriz[i])
        resultado = soma - matriz[i][i]
        if(resultado > matriz[i][i]):
            contador += 1
    return contador

def metodoJacobi(A, b, e, maximoIteracoes):
    verificarA = verificarMatrizDiagonal(A)
    if verificarA > 0:
        print("A não é matriz diagonal!")
    else:
        # np.zeros_like(b): retorna uma matriz com a mesma forma e tipo de (b)
        x = np.zeros_like(b)
        for i in range(maximoIteracoes):
            print("iter. " f"{i} = ", x)
            x0 = np.zeros_like(x)
            # print("teste %d" %A.shape[0])
            for j in range(len(A)):
                # s1 e s2: operação para calcular C, tal que x[j+1] = cx[j] + g
                s1 = np.dot(A[j, :j], x[:j])
                s2 = np.dot(A[j, j + 1:], x[j + 1:])
                x0[j] = (b[j] - s1 - s2) / A[j, j]
                # np.dot: produto escalar
                # A[j, :j]: retorna o vetor de elementos à esquerda do A[j, j], da mesma linha
                # x[:j]: vetor de elementos à esquerda de x[j]
                # x[j+1:]: vetor de elementos à direita de x[j+1]



            
            # np.allclose: retorna True se as matrizes x e x0 são
            # iguais em termos de elementos dentro da erro.
            if np.allclose(x, x0, atol=e, rtol=0.):
                break

            x = x0

        print(" ")
        print("resultadoado:")
        for i in range(len(x)):
            print("%.4f\t" %x[i], end="")
        # print(x)



A = np.array(
    [
        [10.0, 2.0, 1.0],
        [1.0, 5.0, 1.0],
        [2.0, 3.0, 10.0]
    ]
)
print("teste:")
b = np.array(
    [7.0, -8.0, 6.0]
)
metodoJacobi(A,b, 0.0163, 100)

print("-----------------------------------")

