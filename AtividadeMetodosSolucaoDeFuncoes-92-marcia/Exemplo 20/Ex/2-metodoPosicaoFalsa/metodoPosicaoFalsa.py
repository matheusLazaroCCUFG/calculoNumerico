import math
maximoIteracoes = 17

def funcao(x):
    return (4*math.sin(x) - math.exp(x))

def metodoPosicaoFalsa(a, b):
    if(funcao(a) * funcao(b) >= 0):
        print("A condição f(a) * f(b) < 0 deve ser respeitada!")
        return -1

    c = a # Inicialização do resultado
    erro = 0.370562817
    i = 1
    while ((b - a) >= erro):
        # if(i == maximoIteracoes + 1): # não converge
        #  break

        c = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))

        if (funcao(c) == 0):
            break
        elif (funcao(c) * funcao(a) < 0):
            b = c
        else:
            a = c

        i += 1

    print("====================")
    print("Raiz da funcao: x = ", "%.8f" % c)
    print("f(x)", "%.20f" % (funcao(c)))
    print("Erro em x = ", "%.9f" % (erro))
    print("Número de Iterações = ", "%d" % (i - 1))



a = 0
b = 1
metodoPosicaoFalsa(a, b)

    