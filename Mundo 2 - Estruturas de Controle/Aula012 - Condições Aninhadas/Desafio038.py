# Desafio 038: Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
'''
- O primeiro valor é maior
- O segundo valor é maior
- Não existe valor maior, os dois são iguais
'''

print('-' * 60)
print('{:^60}'.format('Comparativo de números v1.0'))
print('-' * 60)
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
print('-' * 60)
print('')

if n1 < n2:
    print(f'{n1} é menor que {n2}.')
elif n1 > n2:
    print(f'{n1} é maior que {n2}.')
else:
    print(f'{n1} é igual a {n2}.')

print('')
print('-' * 60)