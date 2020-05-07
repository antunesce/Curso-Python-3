# Desafio 017: Faça um programa que leia o comprimento do cateto oposto e do cateto adjascente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math
cateto_adj = float(input('Digite o comprimento do Cateto Adjascente, em metros (m): '))
cateto_op = float(input('Digite o comprimento do Cateto Oposto, em metros (m): '))

hipotenusa = math.hypot(cateto_adj, cateto_op)

print(f'A Hipotenusa é {hipotenusa:0.2f}m.')
