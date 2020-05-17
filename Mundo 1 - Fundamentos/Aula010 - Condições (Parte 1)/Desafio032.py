# Desafio 032: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

from datetime import date # Módulo de datas

print('-' * 70)
print('{:^65}'.format('Identificador de ano Bissexto'))
print('-' * 70)
ano = int(input('Digite o ano a ser verificado (digite 0 caso queira o ano atual): '))
print('-' * 70)
print('')

if ano == 0:
    ano = date.today().year # Irá atribuir o ano atual a variável ano

if ano % 4 == 0 and ano % 400 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO.')
else:
    print(f'O ano {ano} não é BISSEXTO')

print('')
print('-' * 70)
