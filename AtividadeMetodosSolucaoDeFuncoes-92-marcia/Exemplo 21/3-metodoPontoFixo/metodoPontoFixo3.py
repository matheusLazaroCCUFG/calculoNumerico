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

            ---------------------------------------
            Descrição 2 do método do ponto fixo

            * É um método para encontrar a raiz real de uma equação
            não linear por aproximação sucessiva
            * Requer uma estimativa inicial para começar
            * Por ser um método aberto, sua convergência não é garantida

            * Para encontrar a raiz da equação não linear:
                * f(x) = 0
                * Escrevemos f(x) = 0, em que x = g(x)
            * Se x0 é estimativa inicial, a próxima raiz é aproximada
            neste método é obtida por:
            x1 = g(x1)
            * A próxima raiz aproximada é obtida usando do valor de x1:
                * x2 = g(x2)
            * O processo é repetido até obtermos raízes com a precisão
            desejada.

            * Para convergência, os seguintes critérios devem ser
            satisfeitos:
                * | g'(x) | < 1

'''
import math

def funcao(x):
    return (x * math.log(x, 10) - 1)

def funcao2(x):
    return (x - (1.3)*(x*math.log(x, 10) - 1))

def metodoPontoFixo():
    etapa = 1

    x0 = 2.5
    erro = 0.000000038426
    N = 50
    x1 = x0

    while(abs(funcao(x1)) > erro):
        x1 = funcao2(x0)

        x0 = x1
        
        print("Etapa: ", "%d" % etapa)
        print("x0: ", "%.6f" % x0)
        print("f(x0): ", "%.20f" % funcao((x0)))
        print("x1: ", "%.6f" % x1)
        print("-----------------")
        
        #if (etapa >= N):
         #   break
        
        etapa += 1

        

    print("Raiz da funçao: x = ", "%.9f" %x1)
    print("f(x) =  ", "%.20f" %(funcao(x1)))
    print("Número de iterações = ", "%d" %(etapa))


metodoPontoFixo()


