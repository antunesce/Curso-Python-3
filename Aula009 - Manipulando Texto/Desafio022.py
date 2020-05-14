# Desafio 022: Crie um programa que leia o nome completo de uma pessoa e mostre

# 1. O nome com todas as letras maiúsculas.
nome = input('Digite o seu nome completo: ').strip()

nome_lista = nome.split()
nome_final = ' '.join(nome_lista).title()

print(f'Seu nome completo é {nome_final}.')
print(f'Seu nome todo maiúsculo é {nome_final.upper()}.')

# 2. O nome com todas as letras minúsculas.
print(f'Seu nome em minúsculo é {nome_final.lower()}.')

# 3. Quantas letras ao todo (sem considerar os espaços).
nome_junto = ''.join(nome_lista)
quantidade_letras = len(nome_junto)

print(f'Seu nome completo possue {quantidade_letras} letras.')

# 4. Quantas letras tem o primeiro nome.
primeiro_nome = len(nome_lista[0])
print(f'Seu primeiro nome é {nome_lista[0]} e possue {primeiro_nome} letras.')
