import math

def funcao(x):
    return math.cos(x) - 3*x + 1

def derivadaFuncao(x): # usar o simpy
    return -math.sin(x) - 3

def funcao2(x):
    return (1 + math.cos(x))/3

def metodoPontoFixo():
    etapa = 1

    x0 = 1
    e = 0.000001
    N = 10

    while(1):
        # x1 = funcao2(x0)
        x1 = x0 - funcao(x0) / derivadaFuncao(x0)

        print("Etapa: ", "%d" % etapa)
        print("x0: ", "%.6f" % x0)
        print("f(x0): ", "%.6f" % funcao((x0)))
        print("x1: ", "%.6f" % x1)
        print("-----------------")
        x0 = x1
        etapa += 1

        if (etapa > N):
            print("Nao convergente.")

        if (abs(funcao(x1)) <= e):
            break

    print("Raiz da funçao: ", "%.6f" %x1)


metodoPontoFixo()


