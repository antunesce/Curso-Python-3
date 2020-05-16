# Desafio 011: Faça um programa que leia a altura e a largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².

print('*' * 40)
print('       Calculadora de tinta')
print('*' * 40)
print('Qual a dimensão da parede que pretende pintar?')
altura_parede = float(input('Qual a altura da parede em metros? '))
largura_parede = float(input('Qual a largura da parede em metros? '))
tinta_m2 = float(input('Quantos l/m² a tinta escolhida pinta? '))

area_parede = altura_parede * largura_parede
litros_necessarios = area_parede / tinta_m2

print(f'A área a ser pintada é de {area_parede:0.1f}, sendo necessário {litros_necessarios:0.1f} l de tintas.')
