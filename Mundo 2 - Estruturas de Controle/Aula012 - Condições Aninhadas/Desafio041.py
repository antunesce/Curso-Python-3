# Desafio 041: A confederação de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
'''
- Até 9 anos: Mirim
- Até 14 anos: Infantil
- Até 19 anos: Junior
- Até 20 anos: Sênior
- Acima: Master
'''

print('-' * 60)
print('{:^60}'.format('Classificador categórico'))
print('-' * 60)
ano_nascimento = int(input('Digite a sua data de nascimento (19XX): '))
print('-' * 60)
print('')

from datetime import date

ano = date.today().year
idade = ano - ano_nascimento

print(f'O atleta tem {idade} ano(s) de idade.')
if idade <= 9:
    print(f' Você está na catergoria MIRIM.')
elif idade <= 10:
    print(f'Você está na categoria INFANTIL.')
elif idade <= 19:
    print('Você está na catergoria JUNIOR.')
elif idade == 20:
    print('Você está na categoria SÊNIOR.')
else:
    print('Você está na categoria MASTER.')
print('')
print('-' * 60)
