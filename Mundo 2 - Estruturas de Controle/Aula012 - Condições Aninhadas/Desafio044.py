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
print('')

print('=' * 60)
print('{:^60}'.format('Forma de pagamento'))
print('=' * 60)
print('1 - à vista dinheiro/cheque')
print('2 - à vista no cartão')
print('3 - parcelado')
print('')
opcao = int(input('Digite a opção: '))
print('=' * 60)

if opcao == 1:
    print('{:^60}'.format('Opção selecionada: "à vista dinheiro/cheque"'))
    print('=' * 60)
    print('')
    desconto = valor * 10 / 100
    valor_final = valor - desconto
    print(f'Valor bruto:                (=) R$ {valor:0.2f}')
    print(f'Valor do desconto (10%):    (-) R$ {desconto:0.2f}')
    print('')
    print(f'Valor total a pagar:        (=) R$ {valor_final:0.2f}')
elif opcao == 2:
    print('{:^60}'.format('Opção selecionada: "à vista no cartão"'))
    print('=' * 60)
    print('')
    desconto = valor * 5 / 100
    valor_final = valor - desconto
    print(f'Valor bruto:                (=) R$ {valor:0.2f}')
    print(f'Valor do desconto (5%):     (-) R$ {desconto:0.2f}')
    print('')
    print(f'Valor total a pagar:        (=) R$ {valor_final:0.2f}.')
elif opcao == 3:
    print('{:^60}'.format('Opção selecionada: "parcelado"'))
    print('=' * 60)
    parcelas = int(input('Quantidade de parcelas: '))
    print('=' * 60)
    print('')
    if parcelas <= 2:
        valor_das_parcelas = valor / parcelas
        print(f'Valor bruto:            (=) R$ {valor:0.2f}')
        print(f'{parcelas} parcela(s)            (x) R$ {valor_das_parcelas:0.2f}')
        print('')
        print(f'Valor total a prazo:    (=) R$ {valor:0.2f}')
    else:
        juros = valor * 20 /100
        valor_final = valor + juros
        valor_das_parcelas = valor_final / parcelas
        print(f'Valor bruto:            (=) R$ {valor:0.2f}')
        print(f'Juros                   (+) R$ {valor_final - valor}')
        print(f'{parcelas:<2} Parcela(s)           (x) R${valor_das_parcelas: 0.2f}')
        print(f'')
        print(f'Valor total a prazo     (=)R$ {valor_final:0.2f}')
else:
    print('')
    print('\033[1;31mOpção inválida!\033[m')
print('')
print('-' * 60)
