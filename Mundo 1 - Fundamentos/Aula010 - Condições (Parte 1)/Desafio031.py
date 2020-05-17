# Desafio 031: Desenvolva um programa que pergunte a distância de uma viagem em km. Calcule o preço da passagem, cobrando R$ 0,50 por km para viagens até 200 km e R$ 0,45 para viagens mais longas.

print('-' * 60)
print('{:^60}'.format('Calculadora de quilometragem v1.0'))
print('-' * 60)
km = float(input('Digite a quilometragem percorrida: '))
print('-' * 60)
print('')
if km <= 200:
    valor = km * 0.5
    print(f'Você percorreu {km:0.1f} km, o valor a ser pago é R$ {valor:0.2f}.')
else:
    valor = km * 0.45
    print(f'Você percorreu {km:0.1f} km, o valor a ser pago é R$ {valor:0.2f}.')
print('')
print('-' * 60)
