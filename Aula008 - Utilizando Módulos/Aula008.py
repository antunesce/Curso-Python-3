'''
***Trabalhando com módulos.***

Os programas em Python, por padrão, vem com um conjunto limitado de comandos, para permitir que o programa seja leve e não ocupe muito espaço na memória.
Todavia, caso seja necessário, pode-se fazer a utilização de bibliotecas importando-as ao programa, passando à funcionar junto ao programa.
Para incluir algo dentro do Python utiliza-se a função "import(nome do módulo ou biblioteca)", nesse caso ao importar a biblioteca, todas as funções serão importadas, mesmo que você não vá utilzar todas.
    import nome da bibliote 

Para importar só a função que se quer utliza-se o comando "from nome da biblioteca import o nome da função", nesse caso só será importada apenas uma função específica.
    from nome da biblioteca import função

***módulo "math"***
É um módulo com funções matemáticos.
Existem diversas funções dentro do módulo "math" como:
    ceil - arredonda os números para cima
    floor - arredonda os números para baixo
    trunc - ele trunca um número, ou seja, ele elimina os números após a vírgula
    pow - que calcula a potência
    sqrt - calcula a raíz quadrada
    factorial - calcula a fatorial de um número

Ao utilizar o comando:
    import_math # todas as funções do módulo 'math' serão importados.

Ao utilizar o comando:
    from math import sqrt # importará apenas a função 'sqrt'.
"from match" # é a sintaxe para indicar de onde será importada a função, nesse caso será do módulo 'match'.
"import sqrt" # é a sintaxe para indicar que a função que será importada. nesse caso será a função 'sqrt'.
"import sqrt, ceil" # nessa sintaxe serão importadas duas funções 'sqrt' e 'ceil', para adicionar mais de uma função ao mesmo tempo é só utilizar a vírgula.

Exemplo 1:
    import math # Ao utilizar dessa forma são carregas todas as funções do móculo e é necessário especificar o nome do módulo e da função, "math.sqrt()".
    from math import sqrt, ceil, floor  # Ao utilizar dessa forma não é mais preciso digitar "math.função()". Pode ser digitada diretamente a função, função().
    
    import math
    numero = int(input('Digite um número: '))
    raiz = math.sqrt(numero)
    print(f'A raiz de {numero} é igual a {raiz}')
    print(f'A raiz de {numero} é igual a {math.ceil(raiz)}.')
    print(f'A raiz de {numero} é igual a {math.floor(raiz)}')

    from math import sqrt, ceil, floor
    numero = int(input('Digite um número: '))
    raiz = sqrt(numero)
    print(f'A raiz de {numero} é igual a {raiz}')
    print(f'A raiz de {numero} é igual a {ceil(raiz)}.')
    print(f'A raiz de {numero} é igual a {floor(raiz)}')

Para consultar quais bibliotecas estão disponiveis para serem importadas.
acessar o site do python.org > DOCS > Escolher a verão do Python > Library Reference

Exemplo 2:
    import random
    numero = random.random() # a função "random()" gera um número aleatório entre 0 e 1.
    numero = random.randint(1, 10) # gera um número aleatório inteiro (int) entre 1 e 10 (1, 10).
    print(numero)
!!! ao digitar um comando e segurar crtl + espaço, abre uma lista de opções que podem ser utilizadas.

Algumas bibliotecas vem como padrão junto com o programa e para acessá-las é só executar o comando "import", porém algumas bibliotecas podem não vem como padrão.
acessar o site do python.org > PyPI > Browse packages > Escolher pelo tema que você quer escolher um módulo
Para instalar algum módulo, File > Settings > Project: CursoemVideo > clicar em + e selecionar o módulo.

Exemplo 3:
    import emoji
    print(emoji.emojize("Olá mundo :earth_americas:", use_aliases=True))
    use_aliases=TRUE permite que o desenho do emoji aparece, senão for digitado aparecerá só o código.
'''
