from pylab import *
import math
def funcao(x):
    y = x**3 - 9*x + 3
    return y


x = linspace(0, 1, 1000) # retorna um vetor de 2 elementos, com números de 0 a 1,

def derivada(x):
    h = 0.0001
    derivada = (funcao(x + h) - funcao(x)) / h
    return derivada

def metodoNewtonRaphson(x):
    return (x - (funcao(x) / derivada(x)))

def iteracao(p, n):
    x = p
    for i in range(n):
        x = metodoNewtonRaphson(x)
    return x

print("raiz: ", "%.9f" %iteracao(0, 2))
print("f(x): ", "%.9f" %funcao(iteracao(0, 2)))

plot(x, funcao(x))
grid(True)
show()