# Desafio 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

from math import radians, sin, cos, tan
angulo = float(input('Digite um ângulo qualquer: '))

angulo_radius = radians(angulo) # radians(), converte ângulo em radianus.

print(f'O seno é {sin(angulo_radius):0.2f}. \nO consseno é {cos(angulo_radius):0.2f}. \nA tangente é {tan(angulo_radius):0.2f}.')
