'''
No Python existem vários tipos primitivos, os 4 mais básicos são:

int = Representa valores numéricos negativo ou positivo, sem casa decimal, ou seja, valores inteiros. ex.: 7, -4, 0, 9875
float = Representa valores numéricos negativo ou positivo, com casa decimal, ou seja, valores reais. Também são chamados de ponto flutuante. ex.: 4.5, 0.076, -15.223, 7.0
bool = Representa valores booleanos, assumindo apenas dois estados, True ou False (as primeiras letras sempre devem ser escritas em maiusculas.). Pode ser representado apenas um bit (que aceita apenas 1 ou 0).
str = Representa uma sequencia de um ou mais caracteres, colocamos os valores do tipo TEXTO entre aspas (''). ex.: 'Olá', '7.5', ''(string vazia)

O comando 'print()', pode ser escrito de uma outra forma:
print('A soma vale {}.'.format(s))
as chaves '{}' são chamdas de máscaras e serão substituidas por um método da própria string.
No exemplo a variável 's' será substituida nas chaves '{}' que foram inseridas na string.

Outro método que pode ser utilizado dentro do comando 'print()' é o 'type()'.
o 'type()' retorna a informação referente ao tipo primitivo pertencente da variável.
ex.: nome = input('Qual seu nome? ')
ex.: n1 = input('Digite um número: ')
ao executar o comando 'print(type(nome))' ou 'print(type(n1))', ambas as respostas serão '<class str>'.
n1 = input('Digite um número: ')
print(type(n1))
<class 'str'>

Ao utilizar o comando 'int()', será feita uma conversão de tudo que estiver dentro dos parênteses.
n2 = int(input('Digite um número: '))
print(type(n2))
<class 'int'>
'''

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'. format(n1, n2, s))

'''
***String Methods***

print("variável".isnumeric())

.isnumeric(), Retorno True se todos os caracteres da string forem caracteres NUMÉRICOS e houver pelo menos um caractere, caso contrário, False.
.isalnum(), Retorno True se todos os caracteres da sequência forem ALFANUMÉRICOS e houver pelo menos um caractere, caso contrário, False
.isalpha(), Retorno True se todos os caracteres da sequência forem ALFABÉTICOS e houver pelo menos um caractere, caso contrário, False
.isdecimal(), Retorno True se todos os caracteres da string forem decimais e houver pelo menos um caractere, caso contrário, False.
.islower(), Retorno True se todos os caracteres em caixa 4 da string estiverem em MINÚSCULAS e houver pelo menos um caractere em caixa, caso contrário, False.
.isupper(), Retorno True se todos os caracteres em caixa 4 da cadeia de caracteres estiverem em MAIÚSCULAS e houver pelo menos um caractere em caixa, caso contrário, False.
.isspace(), Retorno True se houver apenas caracteres de espaço em branco na string e houver pelo menos um caractere, caso contrário, False.
.istitle(), Retorno True se a sequência for uma sequência com título e houver pelo menos um caractere, por exemplo, caracteres maiúsculos podem seguir apenas caracteres não-maiúsculos e minúsculos e somente caracteres maiúsculos. Retorne False caso contrário.

fonte: https://docs.python.org/3/library/stdtypes.html#string-methods
'''

