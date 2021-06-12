# Universidade Federal de Goiás
# março de 2021
# Aluno: Matheus Lázaro Honório da Silva - 201801523
# Disciplina: Cálculo Numérico

'''
    Método da Secante para encontar a raiz de um equação

    * Usado para encontrar a raiz de uma equação f(x) = 0
    * É iniciado a partir de duas estimativas distintas x1 e x2
    par aa raiz
    * Procedimento iterativo com interpolação linear para uma raiz
    * Critério de parada:
        * A diferença entre dois valores intermediários for
        menor que o fator de convergência

    * O metodo da secante contorna a necessidade de se obter a
    derivada do metodo de Newton.
    * Substituimos pelo quociente das diferenças
    f1(xk) = (f(x[k]) - f(x[k - 1])) /
            (x[k] - x[k-1])
    * x[k] e x[k - 1] são aproximações para a raiz
    * φ(x[k]) = (x[k - 1] * f(x[k]) - x[k] * f(x[k - 1]) /
                (f(x[k]) - f(x[k - 1]))

'''
import math

def funcao(x):
    f = (math.exp(-x**2) - math.cos(x)) # 89 Livro Marcia A. Gomes Ruggiero
    return f


def metodoDaSecante(x1, x2, erro):
    numIteracoes = 0 

    if(funcao(x1) * funcao(x2) < 0):
        while True:
            # Resultado da função de iteração, 
            # pelo Quociente das diferenças
            x0 = ((x1 * funcao(x2) - x2 * funcao(x1)) /
                 (funcao(x2) - funcao(x1)))

            c = funcao(x1) * funcao(x0)

            x1 = x2 # Mudança de valores das variáveis
            x2 = x0

            numIteracoes += 1

            if(c == 0):
                break

            # Resultado da função de iteração, 
            # pelo Quociente das diferenças para as novas variáveis
            xm = ((x1 * funcao(x2) - x2 * funcao(x1))/
                  (funcao(x2) - funcao(x1)))

            if(abs(xm - x0) < erro):
                break

        raiz = round(x0, 9) # 9 dígitos de precisão
        print("Raiz da equação = ", raiz)
        print("f(x) = ", "%.9f" %funcao(raiz))
        print("Número de iterações = ", numIteracoes)

        return raiz

    else:
        print("Não foi encontrada raiz neste intervalo!")


x1 = 1
x2 = 2

erro = 0.000018553
raiz = metodoDaSecante(x1, x2, erro)

# raiz = linspace(0, 1, 1000)
