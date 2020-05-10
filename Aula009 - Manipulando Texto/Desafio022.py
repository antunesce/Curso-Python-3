# Desafio 022: Crie um programa que leia o nome completo de uma pessoa e mostre

# 1. O nome com todas as letras maiúsculas.
nome = input('Digite o seu nome completo: ').strip()

nome_sem_espaço = nome.split()
nome_correto = ' '.join(nome_sem_espaço)

print(nome_correto.upper())

# 2. O nome com todas as letras minúsculas.
nome = input('Digite o seu nome completo: ').strip()

nome_sem_espaço = nome.split()
nome_correto = ' '.join(nome_sem_espaço)

print(nome_correto.lower())

# 3. Quantas letras ao todo (sem considerar os espaços).
nome = input('Digite seu nome completo: ').strip()

nome_sem_espaço = nome.split()

print(len(''.join(nome_sem_espaço)))

# 4. Quantas letras tem o primeiro nome.
nome = str(input('Digite o seu nome completo: ')).strip()

nome_completo = nome.title().split()
nome_final = ' '.join(nome_completo)

print(f' O seu nome completo é {nome_final}, seu primeiro nome é {nome_completo[0]} e possue {len(nome_completo[0])} letras.')
