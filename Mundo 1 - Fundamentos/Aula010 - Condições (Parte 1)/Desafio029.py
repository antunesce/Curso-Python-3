# Desafio 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$ 7,00 por km acima do limite.

print('-' * 60)
print('{:^60}'.format('Medidor de velocidade'))
print('-' * 60)
velocidade = float(input('Digite a velocidade do automóvel (km): '))
print('-' * 60)
print('')

if velocidade > 80:
    acima_do_limite = velocidade - 80
    multa = acima_do_limite * 7
    print(f'Você ultrapassou {acima_do_limite:0.1f} km/h, a multa a ser paga é de R$ {multa:0.1f}.')
else:
    print('O motorista não ultrapasou o limite de 80 km/h, Parabéns!')
print('')
print('-' * 60)
