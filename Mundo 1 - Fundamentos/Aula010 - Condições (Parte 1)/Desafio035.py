# Desafio 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

print('-' * 60)
print('{:^60}'.format('Testando a existência de um triângulo'))
print('-' * 60)
l1 = float(input('Digite a medida do primeiro lado: '))
l2 = float(input('Digite a medida do segundo lado: '))
l3 = float(input('Digite a medida do terceito lado: '))
print('-' * 60)
print('')

''' Condição de existência
Para construir um triângulo é necessário que a medida de qualquer um dos lados seja menor que a soma das medidas dos outros dois e maior que o valor absoluto da diferença entre essas medidas.'''

from math import fabs

if (fabs(l2 - l3) < l1 < (l2 + l3)) and (fabs(l1 - l3) < l2 < (l1 + l3)) and (fabs(l1 - l2) < l3 < (l1 + l3)):
    print(f'É possível formar um triângulo de lado {l1}, {l2} e {l3}.')
else:
    print(f'Não é possível formar um triângulo de lado {l1}{l2} e {l3}.')

print('')
print('-' * 60)
