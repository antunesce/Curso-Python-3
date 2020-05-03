# Cadeia de caracteres ou string são sequências de palavras, símbolos e/ou números colocadas entre aspas simples ou duplas.
'''Ex.: 'Curso em vídeo Python'
        "Curso em vídeo Python"
        'Aula 009'  '''
'''Quando se atribui a uma variável uma string esses dados serão armazenados na memória do computador, porém esse espaço
na memória irá ser quebrado em mini-espaços e cada caractere será colocado nesses espaços.
ex.
frase = 'Curso em video Python' <- cada caractere será incluido em um mini espaço e será atribuido uma posição.
C u r s o   e m   v  i  d  e  o     P  y  t h  o  n
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
'''
# Com a separação dos carcteres é possivel fazer alguns tratamentos nessas cadeias como:
# Fatiamento - permite pegar partes das strings
'''ex.: 'frase[9] -> irá mostrar a letra "V" que é o caractere que está na posição 9 dentro da variável "frase".
   ex.: 'frase[9:13] -> o simbolo ":" permite pegar um intervalo de caracteres, nesse caso ele irá pegar o caractere
   da posição 9 (que é onde começará) até o caractere da posição 12 (que é onde terminará), pois ele fará a contagem até
   o caractere da posição 13, mas irá pegar o caracetere anterior ao número final que foi indicado. no exemplo ele irá puxar "Vide".
   ex.: 'frase[9:21] -> não irá dar erro já que a última posição é a 20 e como o comando irá pegar até a posição anteriar
   a pedida (posição :21) dará certo. nesse exemplo será "video Python".
   ex.: 'frase[9:21:2] -> irá do 9 ao 21, porém irá pular de 2 em 2, pegará sempre a segunda posição seguinte. nesse 
   exemplo será "v d o P t o" .
   ex.: 'frase[:5] -> Quando não é indicado a posição inicial indica que começará da primeira posição, a posição 0, até a posição anterior a 5.
   ex.: 'frase[15:] -> Quando não é indicado a posição final, quer dizer que ele iniciará pela posição que você indicou (15)
   e irá até o final da string (última posição).
   ex.: 'frase[9::3] -> irá inicar no 9, como não tem indicação de até onde se quer ele entendi que deve ir até o final,
   indicado pelo, porém irá pular de 3 em 3, pegará sempre a terceira posição seguinte. nesse 
   exemplo será "v e P h" .
'''

# Análise -> É saber informações sobre a string, como saber com qual letra começa, o tamanho da string, qual letra termina.
''' ex.: 'len(frase) -> len vem de length, que significa comprimento, ou seja, ao utilizar este comando ele mostrará o comprimento da string.
    ex.: frase.count('o') -> "frase" é a variável que possui a string. ".count()" é o comando utilizado para contar algo dentro da variável.
    "('o')" indica que será contada as vezes que a letra "o" irá aparecer na string.
    ex.: 'frase.count('o', 0, 13) -> irá contar a quantida da letra 'o' dentro do intervalo 0 a 13, lembrando que contará até a posição anterior
    a última, nesse caso a última posição é a 13 e ele contará até a posição 12.
    ex.:'frase.find('deo') -> ".find()" me mostra a quantidade de vez que ele encontrou algo dentro da string, mostrando em que 
    posição que começou o que se procura dentro da string.
    ex.: 'frase.find('Android')' -> nesse caso ele retornará o valor -1, indicando que não existe a string que você está procurando.
    ex.: 'Curso' in frase -> o operador "in" mostra se existe ou não o que foi pesquisado dentro da string.
'''

# Transformação ->
''' ex: 'frase.replace('Python', 'Android')' -> ".replace()" permite substituir um trecho da string por outro.
".replace('Python', 'Android')" a primeira posição ('Python') indica a string que o operador irá procurar para poder substituir
pela string da segunda posição ('Android'). Se a palavra for maior e tiver que adicionar um espaço ele fará automaticamente.
   ex.: 'frase.upper()' -> irá colocar todas letras em maisculas dentro da string, não irá mexer no que já estiver em maiscúla.
   ex.: 'frase.lower()' -> irá substitir todas as letras maiscúlas em minúsculas.
   ex.: 'frase.capitalaze()' -> esse operador transforma todas as strings em minúsculas e coloca apenas a primera letra de toda a string em maiúscula.
   ex.: 'frase.title()' -> esse operador transforma a primeira letra de cada palavra em maiúscula.
   ex.: 'frase.strip()' -> retira todas os espaços que estão no inicio e no final da string, mantendo os espaços entre palavras.
   ex.: 'frase.rstrip()' -> A letra 'r' em 'rstrip' significa right, ou seja, direita, dessa forma esse comando
   irá retirar todos os espaços a direita da string, todos os espaços do final da string.
   ex.: 'frase.lstrip()' ->  A letra 'l' em 'lstrip' significa left, ou seja, esquerda, dessa forma esse comando irá
   retirar todos os espaços a esquerda da string, ou seja, todos os espaços do inicio da string.
  '''

# Divisão
''' ex.: frase.split() -> irá ocorrer uma divisão dentro da string, considerando os espaços, gerando uma nova indexação.
dividirá uma string em uma lista baseado nos espaços.'''

# Junção
''' ex.: '-'.join(frase) -> irá juntar todos os elementos de frase usando o separador '-'.'''

frase = 'Curso em Video Python'
print(frase[:33])

# Pode ser utilizada as aspas duplas 3x para incluir todo o texto sem precisar colocar cada parte dentro do comando
#  print()
print("""Bem no coração de Lisboa, junto ao Marquês de Pombal, nasceu 
este maravilhoso espaço que ambiciona ser o novo ponto de encontro e 
tertúlia para os aficionados da boa Comida, Vinhos e Petiscos.""")
