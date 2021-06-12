# Universidade Federal de Goiás
# Instituto de Informática - Ciência da Computação - fevereiro de 2021
# Aluno: Matheus Lázaro Honório da Silva - 201801523
# Disciplina: Cálculo Numérico
# Método da Bissecção utilizando Python

# Para a obtenção de solução de uma função em um determinado intervalo
# Podemos considerar um intervalo entre (a) e (b), tais que:
# [f(a) * f(b)] < 0 é contínuo no intervalo fechado [a, b]
# f(x): equação algébrica
# Encontrar a raiz da função em [a, b], ou um valor de x tal que:
# f(x) = 0

'''
    Teoria sobre o método da Bissecção
        * Livro Neide - Cap 3. Equações não lineares

        * Reduz o comprimento do intervalo que contém a raiz,
        de maneira sistemática.
        * Considere o intervalo [a, b] para o qual f(a) * f(b) < 0.
        * No método da bissecção calculamos o valor da função f(x)
        no ponto médio: x1 = (a + b)/2. Portanto, existem três
        possibilidades:
            1) O valor da função calculado no ponto x1 é nulo
                - f(x1) = 0
                - Nessa caso, x1 é o zero da função, então paramos
            2) f(a) * f(b) < 0
                - a função tem um zero entre (a) e x1.
                - O processo é repetido sobre o novo intervalo [a, x1]
            3) f(a) * f(x1) > 0
                - Segue que, f(b) * f(x1) < 0, desde que seja conhecido
                que f(a) e f(b) têm sinais opostos.
                - A função tem um zero entre x1 e b, e o processo
                é repetido com [x1, b]
        A repetição do método é chamado ITERAÇÃO e as aproximações
        sucessivas são os termos iterados.
'''
# Exemplo de função em que a solução é determinada usando
# o método da bissecção
import math
maxIteracoes = 24
def funcao(x):
    return (x * math.log(x, 10) - 1)

def metodoBisseccao(a, b):
    maxIteracoes = 24

    if(funcao(a) * funcao(b) >= 0):
        print("A condição f(a) * f(b) < 0 deve ser verdadeira!\n")
        return

    i = 0
    c = a
    erro = 0.0000000059605
    while(abs(funcao(c)) > erro):  # Erro tolerável
        if(i == maxIteracoes + 1): # não converge
            break
        c = (a + b)/2 # Ponto médio

        if(funcao(c) == 0.0): # Verificar se o ponto médio é raiz
            break

        if(funcao(c) * funcao(a) < 0): # Verificar a condição para retornar ao loooping
            b = c
        else:
            a = c

        i = i + 1

    print("===========================")
    print("Valor da raiz: x = ", "%.8f"%c)
    print("f(x) = ", "%.12lf"%(funcao(c)))
    print("Erro em x = ", "%.9f" %erro)
    print("Número de Iterações = ", "%d" %(i-1))

# Principal / Main
a = 2
b = 3

metodoBisseccao(a, b) 
