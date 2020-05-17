# Desafio 030: Crie um programa que leia um número inteiro qualquer e mostre na tela se ele é PAR ou ÍMPAR.

print('-' * 60)
print('{:^60}'.format('Par ou Ímpar'))
print('-' * 60)
numero = int(input('Digite um número: '))
print('-' * 60)
print('')

if (numero % 2) == 0:
    print(f'Você digitou o número {numero} e é PAR.')
else:
    print(f'Você digitou o número {numero} e é ÍMPAR.')
print('')
print('-' * 60)
