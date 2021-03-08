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
e = 2.71828182846 # constante de Euler

def funcao(x):
      return ((((x+1)** 2) * (math.exp (((x** 2) - 2))))- 1) ## Exemplo do livro - 64
    # return math.sqrt(x) - math.cos(x)
      
    # return (x** 3) - 5*x - 9

def metodoBisseccao(a, b):
    if(funcao(a) * funcao(b) >= 0):
        print("A condição f(a) * f(b) < 0 deve ser verdadeira!\n")
        return

    i = 1
    c = a
    while((b - a) >= 0.00001):  # 0.00001: Erro tolerável
        c = (a + b)/2 # Ponto médio

        if(funcao(c) == 0.0): # Verificar se o ponto médio é raiz
            break

        if(funcao(c) * funcao(a) < 0): # Verificar a condição para retornar ao loooping
            b = c
        else:
            a = c

        print("iter: ", "%d"%i)
        print("a = ", "%d"%a)
        print("b = ", "%d"%b)
        print("xk = ", "%.5f"%c)
        print("f(xk) = ", "%.5f"%(funcao(c)))
        print("--------------------")
        i = i + 1

    print("Valor da raiz: ", "%.5f"%c)

# Principal / Main
## Exemplo do livro - 64
a = 0
b = 1

# a = 2
# b = 3
metodoBisseccao(a, b) 
