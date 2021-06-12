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
        *
'''

# from pylab import *
import math
def funcao(x):
    y = (math.exp(-x**2) - math.cos(x))
    return y


# x = linspace(0, 1, 1000) # retorna um vetor de 2 elementos, com números de 0 a 1,

def derivada(x):
    return math.sin(x) - 2 * x * math.exp(-x**2)
    # h = 0.0017072
    # derivada = (funcao(x + h) - funcao(x)) / h # metodo do quociente
    # return derivada

def metodoNewtonRaphson(x):
    return (x - (funcao(x) / derivada(x)))

def iteracao(p, n):
    x = p
    erro = 0.00017072
    qtdIteracoes = 0
    # for i in range(n): # range: retorna uma sequência e numeros (vetor), de 0 a n
    while(abs(funcao(x)) > erro):
        x = metodoNewtonRaphson(x)
        qtdIteracoes += 1
        
    
    print("raiz: ", "%.9f" %x)
    print("f(x): ", "%.9f" %funcao(x))
    print("Número de Iterações ", qtdIteracoes)



iteracao(1.5, 2)

# plot(x, funcao(x))
# grid(True)
# show()