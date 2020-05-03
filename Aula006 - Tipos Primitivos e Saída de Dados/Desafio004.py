# Desafio 004: Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

v = input("Digite algo: ")

print('Você digitou "{}" e o tipo primitivo que ele percente é {}.'.format(v, type(v)))
print('"{}" é um número? {}.'.format(v, v.isnumeric()))
print('"{}" é um número decimal? {}.'.format(v, v.isdecimal()))
print('"{}" é um número alfanumérico? {}'.format(v, v.isalnum()))
print('"{}" só tem letras do alfabético? {}'.format(v, v.isalpha()))
print('"{}" só tem espaço? {}.'.format(v, v.isspace()))
print('"{}" tem o primeiro caractere em letra maiúscula? {}.'.format(v, v.istitle()))
print('"{}" está todo em minúscula? {}.'.format(v, v.islower()))
print('"{}" está todo em maiúscula? {}.'.format(v, v.isupper()))
