# Universidade Federal de Goias
# março de 2021
# Aluno: Matheus Lázaro Honório da Silva - 201801523
# Disciplina: Cálculo numérico
# MÉTODO DO PONTO FIXO COM PYTHON

'''
    Descrição do método do ponto fixo

    Um ponto fixo para uma função:
        * É um ponto no qual o valor da função não muda quando
        a função é aplicada.
        * X é um ponto fixo para um dada função f se:
            * f(x) = x e 
            * A iteração de ponto fixo x[n+1] = f(x[n])
            

'''

from pylab import plot,show
from numpy import array,linspace,sqrt,sin
from numpy.linalg import norm

def metodoPontoFixo(
    funcao,
    x0,
    tolerancia=0.00001,
    maximoIteracoes=1000000
):
    e = 1
    iteracao = 0
    xp = []
    while(e > tolerancia and iteracao < maximoIteracoes):
        x = funcao(x0)      # fixed point equation
        e = norm(x0-x) # error at the current step
        x0 = x
        xp.append(x0)  # save the solution of the current step
        iteracao = iteracao + 1
    return x,xp



funcao = lambda x : sqrt(x)

x_start = .5
xf, xp = metodoPontoFixo(funcao,x_start)

x = linspace(0,2,100)
y = funcao(x)
plot(
    x,
    y,
    xp,
    funcao(xp),
    'bo',
    x_start,
    funcao(x_start),
    'ro',
    xf,
    funcao(xf),
    'go',
    x,
    x,
    'k'
)
show()


