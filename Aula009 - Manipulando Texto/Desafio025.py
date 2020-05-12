# Desafio 025: Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

nome = input('Digite o seu nome completo: ').strip().title()

nome_split = nome.split()
nonme_corrigido = ' '.join(nome_split)
silva = 'Silva' in nonme_corrigido

print(type(nome))
print(type(nome_split))
print(type(nonme_corrigido))
print(type(silva))