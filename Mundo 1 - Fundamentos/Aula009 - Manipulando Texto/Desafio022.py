# Desafio 022: Crie um programa que leia o nome completo de uma pessoa e mostre

# 1. O nome com todas as letras maiúsculas.
nome = str(input('Digite o seu nome completo: ')).strip()

nome_lista = nome.split()
nome_final = ' '.join(nome_lista).title()

print(f'Seu nome completo é {nome_final}.')
print(f'Seu nome todo maiúsculo é {nome_final.upper()}.')

# 2. O nome com todas as letras minúsculas.
print(f'Seu nome em minúsculo é {nome_final.lower()}.')

# 3. Quantas letras ao todo (sem considerar os espaços).
nome_junto = ''.join(nome_lista)
quantidade_letras = len(nome_junto) # Alternativa para resolver esse problema é 'len(nome_final) - nome_final.count(' ')'. 

print(f'Seu nome completo possue {quantidade_letras} letras.')

# 4. Quantas letras tem o primeiro nome.
primeiro_nome = len(nome_lista[0]) # Alternativa é '.nome_final.find(' ') -> irá dizer qual a posição do primeiro espaço que será a quantidade de letras do primeiro nome.
print(f'Seu primeiro nome é {nome_lista[0]} e possue {primeiro_nome} letras.')
