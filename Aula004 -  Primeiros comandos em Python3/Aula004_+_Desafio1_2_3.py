'''
O símbolo "#" (cerquilha ou reche ou jogo da velha)  é utilizado dentro do Python para escrever comentários, o terminal do Python não vai identificá-lo como um comando a ser executado e irá ignorá-lo.
Pode ser utilizada as aspas simples 3x para colocar um parágrafo todo como comentário
'''

# Desafio 001: Crie um scrit Python que leia o nome de uma pessoa e mostra uma mensagem de boas-vindas de acordo com o valor digitado.
print('========= Desafio 01 ============')
nome = input('Qual é o seu nome? ')
print('Olá ', nome, '! Prazer em te conhecer!')

# Desafio 002: Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.
print('========= Desafio 02 ============')
dia = input('Qual o dia do seu nascimento? ')
mes = input('Qual o mês do seu nascimento? ')
ano = input('Qual o ano do seu nascimento? ')
print('A sua data de nascimento é', dia, '/', mes, '/', ano, '. Correto?')

# Desafio 003: Crie um script Python que leia dois números e tente mostrar a soma entre eles.
print('========= Desafio 03 ============')
print('         VAMOS SOMAR?')
n1 = input('Digite o primeiro número: ')
n2 = input('Digite o segundo número: ')
s = n1 + n2 #O sinal de "+" está servido como uma concatenação e não como o símbolo aritmético de soma, pois os valores ques estão sendo atribuidos as variáveis são strings.
print('A soma vale', s)
# Para solucionar esse problema deve-se colocar o comando 'input()' dentro do comando 'int()', que irá transformar os valores strings em um tipo primitivo chamado int (número inteiro).
# Resolução:
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
s = n1 + n2
print('A soma vale', s)
