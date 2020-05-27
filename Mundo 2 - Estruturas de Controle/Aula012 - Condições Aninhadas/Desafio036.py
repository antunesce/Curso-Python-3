# Desafio 036: Escreva um programa para aprovar um empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('-' * 60)
print('{:^60}'.format('Financiamento imobiliário v1.0'))
print('-' * 60)
valor = float(input('De quando você precisa? R$ '))
salario = float(input('Qual o valor do seu salário? R$ '))
anos = int(input('Digite a quantidade de ano(s): '))
print('-' * 60)
print('')

parcela = anos * 12
valor_parcela = valor / parcela
limite_salario = salario * 30 / 100

if valor_parcela < limite_salario:
    print(f'O seu empréstimo foi \033[1;32mAPROVADO\033[m!')
    print(f'O valor solicitado é de R$ {valor:0.2f}, parcelado em {parcela} x R$ {valor_parcela:0.2f}.')
else:
    print(f'A condição de empréstimo solicitada foi:')
    print(f'Valor solicitado: R$ {valor:0.2f}, em {parcela} parcelas de R$ {valor_parcela:0.2f}')
    print(f'A parcela máxima é de R$ {limite_salario:0.2f}.')
    print(f'Seu empréstimo foi \033[1;31mNEGADO\033[m!')

print('')
print('-' * 60)
