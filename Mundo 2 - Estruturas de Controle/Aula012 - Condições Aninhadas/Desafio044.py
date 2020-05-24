# Desafio 044: Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
'''
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço normal
- 3x ou mais no cartão: 20% de juros
'''

print('-' * 60)
print('{:^60}'.format('Calculadora de pagamento v1.0'))
print('-' * 60)
valor = float(input('Qual o valor do produto R$ '))
print('-' * 60)