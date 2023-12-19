# PAA---Projeto-e-Analise-de-Algoritmos
# Problema-BeeCrowd-2842-Programacao-Dinamica-PAA

O problema exemplo em questão será o problema #2842 ("Dabriel e Suas Strings") da plataforma Beecrowd:
https://www.beecrowd.com.br/judge/pt/problems/view/2842
          DICA: como fazer as entradas e saídas no BeeCrowd, para vários tipos de linguagem: https://www.beecrowd.com.br/judge/pt/faqs/about/examples

⇒ Trabalho em grupo de dois discentes (dupla)

⇒ Descrição:

####################
"Dabriel está brincando com suas duas maravilhosas strings e, ao fazer algumas operações com elas, percebeu uma coisa:
sempre existe uma terceira string que contém como subsequência as suas outras duas strings. Uma subsequência é formada através da remoção de alguns caracteres, e os restantes se mantém na mesma posição relativa. Por exemplo: A string 'casa' contém como subsequência a string 'cs', mas não contém a string 'ac'. Após um tempo analisando essas propriedades, Dabriel percebeu que para gerar a terceira string bastava concatenar as outras duas, uma coisa muito trivial. Portanto, ele solicitou sua ajuda para determinar qual o tamanho da menor string que possui as duas como subsequência.
FORMATO DA ENTRADA:
A primeira linha contém a string A (1 ≤ |A| ≤ 1000), e a segunda linha contém a string B (1 ≤ |B| ≤ 1000). Elas são formadas apenas por letras minúsculas do alfabeto.
FORMATO DA SAÍDA
Informe qual o tamanho da menor string que possui como subsequências as strings A e B.
# Exemplo 1:

Entrada:</br>
casa
casaco

Saída:</br>
6

# Exemplo 2:
Entrada:</br>
bola</br>
bota</br>

Saída:</br>
5


⇒ Requisitos Técnicos:
   * A implementação deve ser feita em uma linguagem de programação de sua escolha.
   * Submeta o código de sua solução na plataforma BeeCrowd (https://www.beecrowd.com.br/judge/pt/problems/view/2842) para verificar a eficácia (corretude) de seu algoritmo.

   * Certifique-se de que sua implementação siga o paradigma da Programação Dinâmica: 

        

    Definir a estrutura do problema: Primeiro, você deve entender claramente o problema que está tentando resolver e definir a estrutura do problema. Identifique as variáveis de estado que descrevem o estado atual do problema.

       

     Identificar a relação de recorrência: Determine como o problema pode ser dividido em subproblemas menores. Isso envolve identificar a relação de recorrência, ou seja, como as soluções dos subproblemas podem ser combinadas para resolver o problema maior.

       

     Definir a função de memória (tabela DP): Crie uma estrutura de dados, como uma matriz, para armazenar as soluções dos subproblemas. Isso é conhecido como a tabela de programação dinâmica (DP table) e ajuda a evitar o recálculo de soluções para os mesmos subproblemas.

       

     Inicialização da DP table: Preencha a DP table com os valores iniciais conhecidos, que são as soluções para os casos base ou subproblemas triviais que podem ser resolvidos diretamente.

       

     Iteração ou recursão: Implemente a iteração ou a função recursiva que percorrerá os subproblemas, calculando e armazenando as soluções em sua DP table. Você deve garantir que cada subproblema seja resolvido antes de ser referenciado novamente.

       

     Construção da solução final: Após preencher a DP table, a solução final do problema estará na entrada correspondente da DP table (geralmente na célula superior direita).

       

     Testar e depurar: Teste sua implementação em várias entradas e verifique se ela produz resultados corretos. Depure quaisquer erros ou problemas de lógica que possam surgir.
