# Desafio 039: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
'''
- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar.
- Se já passou do tempo do alistamento.
'''
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

print('-' * 60)
print('{:^60}'.format('Alistamento militar v1.0'))
print('-' * 60)
ano_nascimento = int(input('Qual o seu ano de nascimento (19XX): '))
print('-' * 60)
print('')

from datetime import date
ano = date.today().year
idade = ano - ano_nascimento

if idade < 18:
    print(f'Você tem {idade} ano(s) de idade. \nFalta(m) {18 - idade} ano(s) para você poder se alistar, em {ano + (18 - idade)}.')
elif idade == 18:
    print(f'Você tem {idade} ano(s) de idade e deve se alistar.')
else:
    print(f'Você tem {idade} ano(s) de idade. \nHá {idade - 18} ano(s) você deveria ter se alistado, em {ano_nascimento + 18}.')

print('')
print('-' * 60)