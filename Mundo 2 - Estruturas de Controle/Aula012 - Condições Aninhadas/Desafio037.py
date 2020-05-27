# Desafio 037: Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
'''
1 - para binário
2 - para octal
3 - para hexadecimal
'''

print('=' * 60)
print('{:^60}'.format('Conversor numérico v1.0'))
print('=' * 60)
number = int(input('Digite um valor a ser convertido: '))
print('=' * 60)
print('''Opções para conversão:
1 - Binário
2 - Octal
3 - Hexadecimal''')
option = int(input('Digite a opção escolhida: '))
print('=' * 60)
print('')

if option == 1:
    number_binary = bin(number)[2:]
    print(f'de Decimal: {number}')
    print(f'para Binário: {number_binary}')
elif option == 2:
    number_octal = oct(number)[2:]
    print(f'de Decimal: {number}')
    print(f'para Octal: {number_octal}')
elif option == 3:
    number_hexdecimal = hex(number)[2:]
    print(f'de Decimal: {number}')
    print(f'para Hexadecimal: {number_hexdecimal}')
else:
    print('Opção inválida!')

print('')
print('=' * 60)
