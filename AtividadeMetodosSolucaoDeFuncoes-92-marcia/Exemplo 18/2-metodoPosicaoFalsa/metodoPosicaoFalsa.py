import math
maximoIteracoes = 50

'''
    Descrição do método da posição falsa
    
    * Dada uma função f(x), x Real  e dois números 'a' e 'b'
    tais que f(a) * f(b) < 0 e f(x) seja contínua em [a, b].
    * f(x) função algébrica
    
    * Semelhanças com o método de bissecção:
    
    * Mesmas premissas: Este método também assume que a função
    é contínua em [a, b] e dados dois números 'a' e 'b' são 
    tais que f (a) * f (b) <0.
     
    * Sempre Converge: como a Bissecção, sempre converge,
    geralmente consideravelmente mais rápido do que a Bissecção
    - mas às vezes muito mais lentamente do que a Bissecção.

    * Diferenças com o Método da Bissecção:
    * Difere no fato de que fazemos um acorde unindo os dois 
    pontos [a, f (a)] e [b, f (b)]. Consideramos o ponto
     em que a corda toca o eixo x e o denominamos c.
     
    * Etapas:

    * Equação da linha que conecta os dois pontos.
        y - f (a) = ((f (b) -f (a)) / (ba)) * (xa)

    * Temos que encontrar o ponto que toca o eixo x. 
        * Para isso, colocamos y = 0.

    * Então x = a - (f (a) / (f (b) -f (a))) * (ba)
       x = (a * f (b) - b * f (a)) / (f (b) -f (a)) 

    * Este será nosso c que é c = x. 

    * Se f (c) == 0, então c é a raiz da solução.
    * Caso contrário, f (c)! = 0
        * Se o valor f (a) * f (c) <0, então a raiz
         fica entre a e c. Então, recorremos para a e c
                  
        * Caso contrário, Se f (b) * f (c) <0, então
         a raiz está entre be c. Portanto, recorremos 
         b e c.
        * Outra função dada não segue uma das suposições.

    * Como a raiz pode ser um número de ponto flutuante
    e pode convergir muito lentamente no pior dos casos,
    iteramos por um grande número de vezes de forma que
    a resposta se torna mais próxima da raiz.
'''

def funcao(x):
    return (math.exp(-x**2) - math.cos(x))

def metodoPosicaoFalsa(a, b):
    if(funcao(a) * funcao(b) >= 0):
        print("A condição f(a) * f(b) < 0 deve ser respeitada!")
        return -1

    c = a # Inicialização do resultado
    erro = 0.552885221
    i = 1
    while((b - a) >= erro):
        # if(i == maximoIteracoes + 1): # não converge
          #  break

        c = (a * funcao(b) - b * funcao(a)) / (funcao(b) - funcao(a))

        if(funcao(c) == 0):
            break
        elif(funcao(c) * funcao(a) < 0):
            b = c
        else:
            a = c

        i += 1

    print("====================")
    print("Raiz da funcao: x = ", "%.8f" %c)
    print("f(x)", "%.9f" %(funcao(c)))
    print("Erro em x = ", "%.9f" %(erro))
    print("Número de Iterações = ", "%d" %(i - 1))



a = 1
b = 2
metodoPosicaoFalsa(a, b)
