'''
***Cadeia de caracteres ou string***
São sequências de palavras, símbolos e/ou números colocadas entre aspas simples ou duplas.
Ex.: 'Curso em vídeo Python'
      "Curso em vídeo Python"
      'Aula 009'

Quando se atribui a uma variável uma string esses dados serão armazenados na memória do computador, porém esse espaço
na memória irá ser quebrado em miniespaços e cada caractere será colocado nesses miniespaços.
Ex.: frase = 'Curso em video Python' <- cada caractere será incluido em um miniespaço e será atribuido uma posição.
C u r s o   e m   v  i  d  e  o     P  y  t h  o  n
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 

Com a separação dos carcteres é possivel fazer alguns tratamentos nessas cadeias como:

# Fatiamento -> permite pegar partes das strings
'variável'[início:fim]
ex.1: 'frase[9] -> irá mostrar a letra "V" que é o caractere que está na posição 9 dentro da variável "frase", porém é o 10º espaço, se contar com o zero.
ex.2: 'frase[9:13] -> o simbolo ":" permite pegar um intervalo de caracteres, nesse caso ele irá pegar o caractere da posição 9 (que é onde começará) até o caractere da posição 12 (que é onde terminará), pois ele fará a contagem até o caractere da posição 13, mas irá pegar o caracetere anterior ao número final que foi indicado. no exemplo ele irá puxar "Vide".
ex.3: 'frase[9:21] -> não irá dar erro já que a última posição é a 20 e como o comando irá pegar até a posição anterior a pedida (posição :21) dará certo. nesse exemplo será "video Python".
ex.4: 'frase[9:21:2] -> irá do 9 ao 21, porém irá pular de 2 em 2, pegará sempre a segunda posição seguinte. nesse exemplo será "v d o P t o".
ex.5: 'frase[:5] -> Quando não é indicado a posição inicial é o mesmo que indicar que começará da primeira posição, a posição 0, até a posição anterior a 5.
ex.6: 'frase[15:] -> Quando não é indicado a posição final quer dizer que ele iniciará pela posição que você indicou (15) e irá até o final da string (última posição).
ex.: 'frase[9::3] -> irá iniciar no 9 e como não tem indicação de até onde se quer, ele entendi que deve ir até o final. O ':3' indica que irá pular de 3 em 3, pegará sempre a terceira posição seguinte. Nesse exemplo será "v e P h".

# Análise -> É saber informações sobre a string, como saber com qual letra começa, o tamanho da string, qual letra termina.
ex.1:'len(frase) -> len() vem de length, que significa comprimento, ou seja, ao utilizar este comando ele mostrará o comprimento da string, contará a quantidade de caracteres que tem dentro da variável.
ex.2: frase.count('o') -> 'frase' é a variável que possui a string. '.count()' é a função utilizada para contar algo dentro da variável. No exemplo, ('o') indica que será contada as vezes que a letra "o" irá aparecer na string.
ex.3: 'frase.count('o', 0, 13) -> irá contar a quantida da letra 'o' dentro do intervalo 0 a 13, lembrando que contará até a posição anterior a última, nesse caso, a última posição é a 13 e ele contará até a posição 12.
ex.4:'frase.find('deo') ' -> '.find()' me mostra a quantidade de vez que ele encontrou algo dentro da string, mostrando em que posição que começou o que se procura dentro da string.
ex.5: 'frase.find('Android')' -> nesse caso ele retornará o valor -1, indicando que não existe a string que você está procurando.
ex.6: 'Curso' in frase -> o operador 'in' mostra se existe ou não o que foi pesquisado dentro da string. Caso exista ele retorna com o valor True, caso contrário retorna com False. 'in' é um operador e não uma funcionalidade, mas serve para fazer análise de string.

# Transformação -> Em regra uma lista de string é imutável, mas é possível mudá-la através de métodos.
ex.1: 'frase.replace('Python', 'Android')' -> '.replace()' permite substituir um trecho da string por outro. '.replace('Python', 'Android')' a primeira posição ('Python') indica a string que o operador irá procurar para poder substituir pela string da segunda posição ('Android'). Se a palavra for maior e tiver que adicionar um espaço ele fará automaticamente.
ex.2: 'frase.upper()' -> 'upper()' irá colocar todas letras em maisculas dentro da string, não irá mexer no que já estiver em maiúscula.
ex.3: 'frase.lower()' -> 'lower()' irá substitir todas as letras maiúsculas em minúsculas, mantendo o que já está em minúscula.
ex.4: 'frase.capitalaze()' -> 'capitalaze()' essa função transforma todas as strings em minúsculas e coloca apenas a primera letra de toda a string em maiúscula.
ex.5: 'frase.title()' -> 'title()' essa função transforma a primeira letra de cada palavra em maiúscula. Essa funação localiza os espaços e faz uma quebra baseado nesses espaços, depois verifica cada pedaço e coloca a primeira letra em maiúscula.
ex.6: 'frase.strip()' -> '.strip()' remove todos os espaços que estão no inicio e no final da string, mantendo os espaços entre palavras.
ex.7: 'frase.rstrip()' -> '.rstrip()' A letra 'r' em 'rstrip' significa right, ou seja, direita, dessa forma esse comando irá remover todos os espaços a direita da string, todos os espaços do final da string.
ex.8: 'frase.lstrip()' -> 'lstrip()' A letra 'l' em 'lstrip' significa left, ou seja, esquerda, dessa forma esse comando irá remover todos os espaços a esquerda da string, ou seja, todos os espaços do inicio da string.
  
# Divisão
ex.1: frase.split() -> '.split()' irá ocorrer uma divisão dentro da string considerando os espaços gerando uma nova indexação. Dividirá uma string em uma lista baseado nos espaços.

# Junção
ex.: '-'.join(frase) -> '.join()' é uma função que irá juntar todos os elementos, tipo string, da variável frase usando o separador '-'.
'''

# Exercício
frase = ('Curso em Vídeo Python')
print(frase.upper().count('O')) # É possível utilizar as funções em cadeia, ou seja, em sequência.

frase = ('Curso em Vídeo Python')
print(frase.capitalize().find('vídeo'))

frase = ('Curso em Vídeo Python')
lista_frase = frase.split()
print(lista_frase[2][2]) # O primeiro [] indica qual o item que está na posição indicada, o segundo [] indica o caractere que está naquela posição do item  da lista.

# Pode ser utilizada as aspas duplas ou simples 3x para incluir todo o texto sem precisar colocar cada parte dentro do comando print().
# print('''Bem no coração de Lisboa, junto ao Marquês de Pombal, nasceu este maravilhoso espaço que ambiciona ser o novo ponto de encontro e tertúlia para os aficionados da boa Comida, Vinhos e Petiscos.''')
