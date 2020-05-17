# Desafio 033: Faça um programa que leia 3 números e mostre qual é o MAIOR e qual é o MENOR.

print('-' * 60)
print('{:^60}'.format('Verificador de número maior e menor'))
print('-' * 60)
n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
n3 = float(input('Digite o terceiro número: '))
print('-' * 60)
print('')

# Testando o maior e o menor número
if n1 > n2 and n1 > n3:
    maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print(f'Número menor: {menor}. \nNúmero maior: {maior}.')
print('')
print('-' * 60)
