# Desafio 019: Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import choice
print('-' * 40)
aluno_1 = input('Digite o nome do aluno de nº 1: ')
aluno_2 = input('Digite o nome do aluno de nº 2: ')
aluno_3 = input('Digite o nome do aluno de nº 3: ')
aluno_4 = input('Digite o nome do aluno de nº 4: ')
print('-' * 40)

print(f'Lista dos alunos:')
print(f'1. {aluno_1}.')
print(f'2. {aluno_2}.')
print(f'3. {aluno_3}.')
print(f'4. {aluno_4}.')
print('-' * 40)

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4] # Lista de variáveis

print(f'O aluno escolhido foi o(a) {choice(lista_alunos)}.')
print('-' * 40)
