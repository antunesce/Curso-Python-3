# Desafio 032: Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO.

ano = int(input('Digite um ano: '))

if (ano / 400) and 4:
    print('Bissexto')
else:
    print('Não')
