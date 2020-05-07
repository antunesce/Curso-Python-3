# Desafio 009: Faça um programa que leia um número qualquer e moste na tela a sua tabuada.

print('*' * 25)
print('         Tabuada')
print('*' * 25)
n = int(input('Tabuada de qual número? '))
print('-' * 25)
print(f'{n} x  1 = {n * 1:2}') # Colocando apenas o :2 (número) irá adicionar casa ao número inteiro.
print(f'{n} x  2 = {n * 2}')
print(f'{n} x  3 = {n * 3}')
print(f'{n} x  4 = {n * 4}')
print(f'{n} x  5 = {n * 5}')
print(f'{n} x  6 = {n * 6}')
print(f'{n} x  7 = {n * 7}')
print(f'{n} x  8 = {n * 8}')
print(f'{n} x  9 = {n * 9}')
print(f'{n} x 10 = {n * 10}')