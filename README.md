# calculoNumerico

# Universidade Federal de Goiás
# Instituto de Informática - Ciência da Computação - Semestre letivo 2020.2 
# Aluno: Matheus Lázaro Honório da Silva - 201801523
# Disciplina: Cálculo Numérico

# Método da Bissecção utilizando Python

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

    
# Método do ponto fixo
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
