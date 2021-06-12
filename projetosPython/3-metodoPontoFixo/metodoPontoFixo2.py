# Universidade Federal de Goias
# março de 2021
# Aluno: Matheus Lázaro Honório da Silva - 201801523
# Disciplina: Cálculo numérico
# MÉTODO DO PONTO FIXO COM PYTHON

'''
    Descrição do método do ponto fixo

    Encontrar as raízes das equações
    pelo método de iteração de ponto fixo

        * Método clássico entre os métodos iterativos
        * Equação de transformação simples
            - Geralmente termo de mudança, quadrado, sinal de raiz, ...
        * Existem dois teoremas no estudo da convergência:
            - Teorema geral:
                + Usado globalmente
                + Quando a equação h(x) é uma função contínua
                no intervalo fechado e no intervalo correspondente.
                + É necessário satisfazer a compressibilidade e a vedação.
                + Fechamento:
                    * Qualquer valor em um determinado intervalo é substituído
                    na função correspondente, e o valor da função obtido também
                    estará neste intervalo.
                + Compressibilidade:
                    *  Existe uma constante menor que 0, de forma que no intervalo
                    correspondente, o valor absoluto da diferença entre os valores
                    da função entre quaisquer dois pontos seja menor que esta
                    constante.
                    * O superior corresponde à diferença de distância entre dois
                    pontos.

            - Teorema Local:
                + Intervalo em torno do ponto fixo
                + h(x):
                    * Valor absoluto da derivada, que deve ser menor que 1
                    * Há uma parde local onde a convergência pode ser alcançada.
                    *

'''

import math
import random

from sympy import symbols

x = symbols("x")
funcao = (x + 1)**(1/3)


def f(x):
    return (x + 1)**(1/3)  ## Exemplo do livro - 64

inicio = 1
fim = 2

maximoIteracoes = 1000

contadorIteracoes = 0

x0 = random.uniform(inicio, fim)
temp = funcao.subs(x, x0)

while contadorIteracoes < maximoIteracoes and abs(temp - x0) > 1e-10:
    x0 = temp
    temp = funcao.subs(x, x0) # substitui x por x0
    contadorIteracoes += 1

print(x0)
print(contadorIteracoes)
print("f(xk) = ", "%.5f" % (f(x0)))


