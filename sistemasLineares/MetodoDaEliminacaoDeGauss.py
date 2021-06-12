N = 3

def metodoDaEliminacaoDeGauss(matriz):
    # obter a redução para a forma escalonada de linha
    # Verifica se há várias soluções, solução única ou infinitas soluções
    flag = eliminacaoF(matriz) # retorna se é singular, ou a linha referente à eliminação

    # matrizriz singular
    if(flag != -1):
        print("matriz singular")

        # Se o lado direito da equação correspondente a
        # linha zero é 0. Posição: 
        # linha: referente à eliminação
        # coluna: N(borda).
        # Sistema com infinitas soluções ou inconsistentes
        if(matriz[flag][N] != 0):
            print("Sistema inconsistente")
        else:
            print("O sistema possui infinitas soluções")
        
        return
    else:
        # Obter solução para o sistema e mostrar
        # usando substituição para trás
        substituicaoParaTras(matriz)

# função para operação de troca entre duas linhas da matrizriz
def trocarLinhas(matriz, i, j):
    #for(k = 0; k <= N; k += 1):
    for k in range(0, N+1): 
        temp = matriz[i][k]
        matriz[i][k] = matriz[j][k]
        matriz[j][k] = temp
    
def eliminacaoF(matriz):
    #for(k = 0; k < N; k += 1):
    for k in range(0, N):
        # Inicializando o valor máximo e índice para o pivô
        indiceMaximo = k
        valorMaximo = int(matriz[indiceMaximo][k])
        
        # Encontrar a maior amplitude para o pivô, se houver
        #for(i = k + 1; i < N; i += 1):
        for i in range(k + 1, N):
            if(abs(matriz[i][k]) > valorMaximo):
                valorMaximo = int(matriz[i][k])
                indiceMaximo = i
        
        # Se o elemento da diagonal principal for zero
        # Denotar que a matriz é singular e
        # Levará a uma divizão por zero posteriormente
        if(matriz[k][indiceMaximo] == 0): # matriz singular
            return k
        
        # Trocar a linha de maior valor com a linha atual da iteração
        if(indiceMaximo != k):
            trocarLinhas(matriz, k, indiceMaximo)

        # Fator f declarado para definir a linha atual
        # k-ésimo elemento até 0 e,
        # k-ésimo aoluna restante até 0
        #for(i = k + 1; i < N; i += 1):
        for i in range(k + 1, N): 
            f = matriz[i][k] / matriz[k][k]

            # Subtrair o múltiplo
            # da linha da atual iteração
            #for(j = k + 1; j <= N; j += 1):
            for j in range(k+1, N+1):
                matriz[i][j] -= matriz[k][j] * f
            
            # Preencher a matriz triangular inferior com zeros.
            matriz[i][k] = 0

    return -1


def substituicaoParaTras(matriz):
    x = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0] 
    # Vetor inicializado para armazenar as soluções

    # Calcular a partir da última equação até a primeira
    #for(i = N - 1; i >= 0; i -= 1):
    for i in range(N-1, -1, -1):
        # Começar pelo Lado direto da equação
        x[i] = matriz[i][N]

        # Inicializando j de i + 1, porque a matriz é triangular superior
        #for(j = i + 1; j < N; j += 1):
        for j in range(i+1, N):
            # Subtrair todos os valores do lado esquerdo
            # exceto o coeficiente da variável
            # cujo valor está sendo calculado
            x[i] -= matriz[i][j] * x[j]

        # Dividir o lado direito pelo coeficiente do desconhecido
        # sendo caldulado
        x[i] /= matriz[i][i]
    
    print()
    print("Solução do sistema:")
    #for(i = 0; i < N; i += 1):
    for i in range(0, N):
        print("%.6f" %x[i])
        

    

def principal():

    '''
        Sistema Exemplo 2 do livro -  Marcia Ruggiero:
        {
            3x1 + 2x2 + 4x3 = 1
            1x1 + 2x2 + 2x3 = 2
            4x1 + 3x2 - 2x3 = 3
        }
    '''
    matriz = [#         A            | b    
            [ 3.0,  2.0,    4.0,    1.0 ],
            [ 1.0,  1.0,    2.0,    2.0 ],
            [ 4.0,  3,      -2.0,   3.0 ] 
    ]
    metodoDaEliminacaoDeGauss(matriz)


    '''
        Sistema Exemplo 7 do livro -  Ruggiero:
        {
            3x1 - 4x2 + 1x3 = 9
            1x1 + 2x2 + 2x3 = 3
            4x1 + 0x2 - 3x3 = -2
        }
    '''
    matriz = [ 
        [ 3,    -4,     1,      9],
        [ 1,    2,      2,      3],
        [ 4,    0,      -3,     -2] 
    ]
    metodoDaEliminacaoDeGauss(matriz)
    
principal()
