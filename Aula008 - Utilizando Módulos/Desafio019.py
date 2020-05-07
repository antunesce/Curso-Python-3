# Desafio 019: Um professor quer sortear um dos seus quatros alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome escolhido.

from random import randint
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
print(f'O número escolhido foi {randint(1, 4)}.')
print('-' * 40)
