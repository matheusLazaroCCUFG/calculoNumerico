import math

def funcao(x):
   f = (x**3 - x - 1) # 89 Livro Marcia A. Gomes Ruggiero
   return f

def metodoDaSecante(x1, x2, erro):
   numIteracoes = 0
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
x1 = 0.0
x2 = 0.5

erro = 0.000008998843
raiz = metodoDaSecante(x1, x2, erro)