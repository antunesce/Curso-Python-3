# Desafio 007: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

print('*' * 48)
print('*' * 13, 'Colégio Mamute feliz', '*' * 13)
print('*' * 48)
print('Vamos calcular a média das notas das avaliações.')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print(f'A média das notas {n1:0.1f} e {n2:0.1f} é {media:0.1f}.')
