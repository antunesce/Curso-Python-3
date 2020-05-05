# Desafio 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('-' * 31)
print(' Calculadora de desconto v.1.0')
print('-' * 31)
valor_original = float(input('Qual o preço do produto? R$ '))
porcentagem_desconto = float(input('Quantos porcentos (%) de desconto? '))


valor_com_desconto = valor_original + (valor_original * porcentagem_desconto / 100)
valor_do_desconto = valor_original * (porcentagem_desconto / 100)
print('-' * 31)
print('')
print(f'O preço do produto sem desconto é R${valor_original}. \nO valor com {porcentagem_desconto:0.0f}% de desconto é R${valor_com_desconto}.')
print(f'Você economizou R${valor_do_desconto}.')
print('')
print('-' * 31)
