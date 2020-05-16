# Desafio 023: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''
Ex.:
Digite um número: 1834
unidade: 4
dezena: 3
centena: 8
milhar: 1
'''

'''
Resolução alternativa
numero = int(input('Digite um número entre 0 e 9999: '))

n = str(numero)

print(f'O número que você digitou foi: {numero}.')
print(f'unidade: {n[3]}.')
print(f'dezena: {n[2]}.')
print(f'centena: {n[1]}.')
print(f'millhar: {n[0]}.')

# Contudo esbarra em um problema, quando o número informado não contém todas as unidades o script dá um erro.
'''
# Solução:

numero = int(input('Digite um número entre 0 e 9999: '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print(f'Você digitou {numero}.')
print(f'unidade: {u}.')
print(f'dezena: {d}.')
print(f'centena: {c}.')
print(f'milhar: {m}.')
