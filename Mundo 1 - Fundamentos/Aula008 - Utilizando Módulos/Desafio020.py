# Desafio 020: O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

import random

print('¬' * 40)
aluno_1 = input('Digite o nome do aluno de nº 1: ')
aluno_2 = input('Digite o nome do aluno de nº 2: ')
aluno_3 = input('Digite o nome do aluno de nº 3: ')
aluno_4 = input('Digite o nome do aluno de nº 4: ')
print('¬' * 40)
print('')
print('Lista dos alunos:')
print(f'1. {aluno_1}.')
print(f'2. {aluno_2}.')
print(f'3. {aluno_3}.')
print(f'4. {aluno_4}.')
print('')
print('-' * 40)

lista_alunos = [aluno_1, aluno_2, aluno_3, aluno_4]
random.shuffle(lista_alunos)

print('')
print(f' A ordem de apresentação de trabalhos é: \n{lista_alunos}.')
print('')
print('¬' * 40)