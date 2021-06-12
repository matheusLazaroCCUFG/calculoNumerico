import math
def funcao(x):
    return (((x - 1)**2 ) * (x - 1.5))

def derivada(x):
    return ((x-1) * (3*x - 4))

def metodoNewtonRaphson(x):
    return (x - (funcao(x) / derivada(x)))


def iteracao(p):
    x = p
    erro = 0.00000001
    qtdIteracoes = 0
    # for i in range(n): # range: retorna uma sequência e numeros (vetor), de 0 a n
    while (abs(funcao(x)) > erro):
        x = metodoNewtonRaphson(x)
        qtdIteracoes += 1

    print("===========================")
    print("Newton")
    print("raiz: ", "%.9f" % x)
    print("f(x): ", "%.30f" %(funcao(x)))
    print("Número de Iterações ", qtdIteracoes)

def metodoBisseccao(a, b):

    if(funcao(a) * funcao(b) >= 0):
        print("A condição f(a) * f(b) < 0 deve ser verdadeira!\n")
        return

    i = 0
    c = a
    erro = 0.001
    while(abs(funcao(c)) > erro):  # Erro tolerável

        c = (a + b)/2 # Ponto médio

        if(funcao(c) == 0.0): # Verificar se o ponto médio é raiz
            break

        if(funcao(c) * funcao(a) < 0): # Verificar a condição para retornar ao loooping
            b = c
        else:
            a = c

        i = i + 1

    c = (a + b) / 2
    print("===========================")
    print("Bissecção")
    print("Valor da raiz: x = ", "%.8f"%c)
    print("f(x) = ", "%.12lf"%(funcao(c)))
    print("Erro em x = ", "%.9f" %erro)
    print("Número de Iterações = ", "%d" %(i-1))

    iteracao(c)

# Principal / Main
a = 0.5
b = 2

metodoBisseccao(a, b)
