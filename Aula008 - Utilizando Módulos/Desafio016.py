# Desafio 016: Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira.

from math import trunc
n = float(input('Digite um número qualquer'))
print(f'A parte inteira do número real {n} é {trunc(n)}.')
