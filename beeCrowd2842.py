# Função que calcula o comprimento da maior subsequência comum entre duas strings
def compSubseq(strA, strB):

    # Guarda o comprimento da primeira string em uma variável
    compA = len(strA)

    # Guarda o comprimento da segunda string em uma variável
    compB = len(strB)

    # Cria uma matriz de zeros com dimensões (compA + 1) x (compB + 1)
    matriz = [[0 for j in range(compB+1)] for i in range(compA+1)]

    # Percorre as linhas da matriz, começando da segunda
    for i in range(1, compA+1):
        # Percorre as colunas da matriz, começando da segunda
        for j in range(1, compB + 1):
            # Se os caracteres nas posições i-1 e j-1 das strings forem iguais
            if strA[i - 1] == strB[j - 1]:
                # Copia o valor da diagonal superior esquerda da matriz e soma um
                matriz[i][j] = matriz[i - 1][j - 1] + 1
            else:
                # Se os caracteres nas posições i-1 e j-1 das strings forem diferentes
                # Copia o maior valor entre o valor acima e o valor à esquerda da matriz
                matriz[i][j] = max(matriz[i - 1][j], matriz[i][j - 1])
        '''for linha in matriz:
            print(" ".join(map(str, linha)))
        print()'''


    # Retorna o valor no canto inferior direito da matriz, que é o comprimento da maior subsequência comum entre duas strings
    return matriz[compA][compB]

# Função que calcula o comprimento da menor string que contém ambas as strings como subsequências
def comprimento(strA, strB):

    # Guarda o comprimento da primeira string em uma variável
    compA = len(strA)

    # Guarda o comprimento da segunda string em uma variável
    compB = len(strB)

    # Chama a função que calcula o comprimento da maior subsequencia comum entre as duas strings
    compLCS_result  = compSubseq(strA, strB)

    # Retorna a soma dos comprimentos das duas strings menos o comprimento do LCS, que é o comprimento do SCS
    return compA + compB - compLCS_result

strA = input()
strB = input()

print(comprimento(strA, strB))