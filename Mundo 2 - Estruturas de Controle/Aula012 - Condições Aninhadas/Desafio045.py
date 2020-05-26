# Desafio 045: Crie um programa que faça o computador jogar JOKENPÔ com você.

import emoji
from random import randint

# Título do script
print('=' * 60)
print('{:^60}'.format('Jokenpô v1.0'))
print('=' * 60)
print('')

# Instruções do game
print('''Instruções:
\033[1;31m1\033[m - \033[1;31mPedra\033[m empata com Pedra e ganha de Tesoura;
\033[1;32m2\033[m - \033[1;32mPapel\033[m empata com Papel e ganha de Pedra;
\033[1;33m3\033[m - \033[1;33mTesoura\033[m empata com Tesoura e ganha de Papel.''')
print('')

# Opção do player
name = str(input('Qual o seu nome: ')).strip().title()
p1 = int(input('Escolha uma das três opções: '))
print('')
print('=' * 60)
print('')

# Opção do NPC
npc = randint(1, 3)

# Teste do game
# Hipótese de vitória
if p1 == 1 and npc == 3:
    print(f'{name} (\033[1;31mPedra\033[m) x (\033[1;33mTesoura\033[m) NPC')
    print('')
    print('Você \033[1;32mVENCEU!!!\033[m')
elif p1 == 2 and npc == 1:
    print(f'{name} (\033[1;32mPapel\033m) x (\033[1;31mPedra\033[m) NPC')
    print('')
    print('Você \033[1;32mVenceu!!!\033[m')
elif p1 == 3 and npc == 2:
    print(f'{name} (\033[1;33mTesoura\033[m) x (\033[1;32mPapel\033[m) NPC')
    print('')
    print('Você \033[1;32mVenceu!!!\033[m')
# Hipotese de derrota
elif p1 == 1 and npc == 2:
    print(f'{name} (\033[1;31mPedra\033[m) x (\033[1;32mPapel\033[m) NPC')
    print('')
    print('Você \033[1;31mPerdeu!!!\033[m')
elif p1 == 2 and npc == 3:
    print(f'{name} (\033[1;32mPapel\033[m) x (\033[1;33mTesoura\033[m) NPC')
    print('')
    print('Você \033[1;31mPerdeu!!!\033[m')
elif p1 == 3 and npc == 1:
    print(f'{name} (\033[1;33mTesoura\033[m) x (\033[1;31mPedra\033[m) NPC')
    print('')
    print('Você \033[1;31mPerdeu!!!\033[m')
# Hipótese de empate
else:
    if p1 and npc == 1:
        p1 = '\033[1;31mPedra\033[m'
        npc = '\033[1;31mPedra\033[m'
    elif p1 and npc == 2:
        p1 = '\033[1;32mPapel\033[m'
        npc = '\033[1;32mPapel\033[m'
    else:
        p1 = '\033[1;33mTesoura\033[m'
        npc = '\033[1;33mTesoura\033[m'
    print(f'{name} ({p1}) x ({npc}) NPC')
    print('')
    print('Houve \033[1;33mEmpate!!!\033[m')

print('')
print('*' * 60)