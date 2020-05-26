# Desafio 045: Crie um programa que faça o computador jogar JOKENPÔ com você.

print('=' * 60)
print('{:^60}'.format('Jokenpô v1.0'))
print('=' * 60)
print('')
print('''Instruções:
\033[1;31m1\033[m - \033[1;31mPedra\033[m empata com pedra e ganha de Tesoura;
\033[1;32m2\033[m - \033[1;32mTesoura\033[m empata com Tesoura e ganha de Papel;
\033[1;33m3\033[m - \033[1;33mPapel\033[m empata com Papel e ganha de Pedra.''')
print('')
p1 = int(input('Escolha uma das três opções: '))
print('')
print('=' * 60)




'''
Papel = :raised_hand_with_fingers_splayed:
pedra = :fist_right: or :fist_left:
tesoura = :v:

win = :smile: :trophy:
loser = :sob:
'''