# Desafio 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número qualquer: '))

dobro = n * 2
triplo = n * 3
raiz = n ** (1/2) # exponencial (** ou pow(n, 1/2))

print(f'O número que você digitou foi {n}.')
print(f'O dobro é {dobro}.')
print(f'O triplo é {triplo}.')
print(f'A raiz quadrada é {raiz:0.2f}.')
