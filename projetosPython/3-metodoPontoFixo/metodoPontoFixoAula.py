# Universidade Federal de Goias
# março de 2021
# Aluno: Matheus Lázaro Honório da Silva - 201801523
# Disciplina: Cálculo numérico
# MÉTODO DO PONTO FIXO COM PYTHON

import math

def funcao(x):
    return math.cos(x) - 3*x + 1

def funcao2(x):
    return (1 + math.cos(x))/3

def metodoPontoFixo():
    etapa = 1

    x0 = 1
    tolerancia = 0.000001
    maxIteracoes = 10

    while(1):
        x1 = funcao2(x0)

        print("Etapa: ", "%d" % etapa)
        print("x0: ", "%.6f" % x0)
        print("f(x0): ", "%.6f" % funcao((x0)))
        print("x1: ", "%.6f" % x1)
        print("-----------------")
        x0 = x1
        etapa += 1

        if (etapa > maxIteracoes):
            print("Nao convergente.")
            break

        if (math.fabs(funcao(x1)) <= tolerancia):
            break

    print("Raiz da funçao: ", "%.6f" %x1)


metodoPontoFixo()


