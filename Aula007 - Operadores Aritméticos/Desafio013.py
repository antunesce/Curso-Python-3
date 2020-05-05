# Desafio 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

print('¬' * 65)
print('                  Folha de pagamento v.1.0')
print('¬' * 65)
print('')
salario = float(input('Digite o valor do salário: R$ '))
porcentagem_aumento = float(input('Qual o percentual (%) de aumento? '))

aumento = (salario * porcentagem_aumento) / 100
salario_aumento = salario + aumento

print('')
print('-' * 65)
print('')
print(f'O salário  de R$ {salario:0.2f} recebeu um aumento de {porcentagem_aumento:0.1f}% (R${aumento:0.2f}).')
print(f'O novo salário é de R${salario_aumento:0.2f}.')
print('')
print('-' * 65)
