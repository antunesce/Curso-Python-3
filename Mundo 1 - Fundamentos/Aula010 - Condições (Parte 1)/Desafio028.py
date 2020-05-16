# Desafio 028: Escreva um programa que faço o computador pensar em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o númro escolhido pelo computador. 
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
print('-' * 60)
print('{:^60}'.format('Jogo do Adivinha qual o número'))
print('-' * 60)
numero = int(input('Vamos brincar de adivinhar, escolha um número de 0 a 5: '))

numero_aleatorio = randint(0, 5)

print('-' * 60)
print('')
if numero == numero_aleatorio:
    print('Parabéns, você acertou! :D')
    print(f'Você escolheu {numero} e o computador {numero_aleatorio}.')
else:
    print('Pennnn, você errou! :p')
    print(f'Você escolheu {numero} e o computador {numero_aleatorio}.')
print('')
print('-' * 60)