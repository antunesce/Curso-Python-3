# No Python existem vários tipos primitivos, os 4 mais básicos são:
# int = Representa valores numéricos negativo ou positivo, sem casa decimal, ou seja, valores inteiros. ex.: 7, -4, 0, 9875
# float = Representa valores numéricos negativo ou positivo, com casa decimal, ou seja, valores reais. Também são chamados de ponto flutuante. ex.: 4.5, 0.076, -15.223, 7.0
# bool = Representa valores booleanos, assumindo apenas dois estados, True ou False (as primeiras letras sempre devem ser escritas em maiusculas.). Pode ser representado apenas um bit (que aceita apenas 1 ou 0).
# str = Representa uma sequencia de um ou mais caracteres, colocamos os valores do tipo TEXTO entre aspas (''). ex.: 'Olá', '7.5'

# O comando 'print()', pode ser escrito de uma outra forma:
# print('A soma vale {}.'.format(s))
# as chaves '{}' são chamdas de máscaras e serão substituidas por um método da própria string.
# No exemplo a variável 's' será substituida nas chaves '{}' que foram inseridas na string.

# outro método que pode ser utilizado dentro do comando 'print()' é o 'type()'.
# o 'type()' retorna a informação referente ao tipo primitivo pertencente da variável.
# ex.: nome = input('Qual seu nome? ')
# ex.: n1 = input('Digite um número: ')
# ao executar o comando 'print(type(nome))' ou 'print(type(n1))', ambas as respostas serão '<class str>'.
#n1 = input('Digite um número: ')
#print(type(n1))
# <class 'str'>

# Ao utilizar o comando 'int()', será feita uma conversão de tudo que estiver dentro dos parênteses.
#n2 = int(input('Digite um número: '))
#print(type(n2))
# <class 'int'>

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2
print('A soma entre {} e {} vale {}'. format(n1, n2, s))

# Outro comando do 'print()'
# 'print(variável.isnumeric())'
# O 'is.numeric()' retornará com o valor lógico da variável perguntada.
# Ele faz um teste para saber se o valor que foi atribuido à variável é um número ou não, True ou False.
# Tem também o 'isalpha()', retorna o valor lógico da variável se é alphabetic.
# Tem também o 'isalnum()', retorna o valor lógico da variável se é alphanumeric.
# Tem também o 'isupper()', retorna o valor lógico da variável se está tudo em letra maiúscula.

