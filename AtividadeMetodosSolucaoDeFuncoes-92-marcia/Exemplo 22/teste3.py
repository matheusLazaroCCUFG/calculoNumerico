# Universidade Federal de Goiás
# março de 2021
# Aluno: Matheus Lázaro Honório da Silva
# Disciplina: Cálculo Numérico

'''
    Método de Newton Raphson

    * Dada uma função f(x), sendo x pertencente aos Reais.
    * f(x) é equação algébrica.
    * A derivada é fornecida como entrada.

    * No método da bisseccao:
        * Recebíamos um intervalo.
        * Tem garantia para convergir.
    * No método de Newton Raphson.
        * Recebemos um valor estimado inicial da raiz.
        * Pode não convergir em alguns casos.
        * Requer derivada, o que pode ser trabalhoso computacionalmente.
        * Normalmente, converge mais rápido.

    * A fórmula:
        * Começando da estimativa inicial x[1] , o método de Newton Raphson
        usa a fórmula abaixo para encontrar o próximo valor de x, ou seja,
        x[n + 1] do valor anterior x[n]

        x[n+1] = x[n] - f(x[n])/
                        f'(x[n])
    * Notas:
        * Geralmente usamos esse método para melhorar o resultado obtido
        pelo método da bissecção ou pelo método da posição falsa.
        * O método babilônico para raiz quadrada é derivado do método
        de Newton-Raphson
'''

# from pylab import *
import math


def funcao(x):
    y = (((x - 1)**2 ) * (x - 1.5))
    return y


# x = linspace(0, 1, 1000) # retorna um vetor de 2 elementos, com números de 0 a 1,

def derivada(x):
     return ((2*(x - 3/2)*(x-1))+(x-1)**2)
     #return ((x-1) * (3*x - 4))
     #h = 0.0000000000017072
     #derivada = (funcao(x + h) - funcao(x))/ h # metodo do quociente
     #return derivada


def metodoNewtonRaphson(x):
    return (x - (funcao(x) / derivada(x)))


def iteracao(p):
    x = p

    erro = 0.0000035082
    qtdIteracoes = 0
    # for i in range(n): # range: retorna uma sequência e numeros (vetor), de 0 a n
    while (abs(funcao(x)) > erro):
        x = metodoNewtonRaphson(x)
        qtdIteracoes += 1


    print("raiz: ", "%.9f" % x)
    print("f(x): ", "%.20f" % (funcao(x)))
    print("Número de Iterações ", qtdIteracoes)


iteracao(1.33334)

# plot(x, funcao(x))
# grid(True)
# show()