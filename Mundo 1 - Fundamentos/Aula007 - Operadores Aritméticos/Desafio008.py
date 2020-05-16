# Desafio 008: Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milímetros.

print('*' * 42)
print('   Calculadora de medida de comprimento')
print('*' * 42)
valor = float(input('Digite um valor em metros: '))

km = valor / 1000
hm = valor / 100
dam = valor / 10
dm = valor * 10
cm = valor * 100
mm = valor * 1000

print(f'Tabela de conversão de medidas de comprimento em metros (m).')
print(f'Você digitou {valor:0.2f} m.')
print(f'em quilômetros - {km:0.2f} km.')
print(f'em hectômetros - {hm:0.2f} hm.')
print(f'em decâmetros  - {dam:0.2f} dam.')
print(f'em metros      - {valor:0.2f} m.')
print(f'em decimétros  - {dm:0.2f} dm.')
print(f'em centímetros - {cm:0.2f} cm.')
print(f'em milímetros  - {mm:0.2f} mm.')
