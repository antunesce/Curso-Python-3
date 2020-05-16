# Desafio 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$ 1.250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%

print('-' * 60)
print('{:^60}'.format('Calculadora de Remuneração v1.0'))
print('-' * 60)
salario = float(input('Digite o valor do salário R$ '))
print('-' * 60)
print('')

if salario > 1250.00:
    aumento = salario * 10 / 100
    print(f'Você recebeu R$ {aumento:0.2f} de aumento.\nSeu salário agora é de R$ {salario + aumento:0.2f}.')
else:
    aumento = salario * 15 / 100
    print(f'Você recebeu R$ {aumento:0.2f} de aumento.\nSeu salário agora é de R$ {salario + aumento:0.2f}.')
print('')
print('-' * 60)
