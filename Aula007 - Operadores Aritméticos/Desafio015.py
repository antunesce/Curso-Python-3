# Desafio 015: Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

print('¬' * 80)
print('                     Calculadora de corrida - TAXIDRIVER v.1.0')
print('¬' * 80)
print('')
dia = int(input('Digite a quantidade de dias alugado: '))
km = float(input('Digite a quantidade de quilométros (km) utilizado: '))

valor_total_km = km * 0.15
valor_total_dia = dia * 60
valor_total_pagar = valor_total_dia +  valor_total_km

print('')
print('-' * 80)
print(f' Você permaneceu com o carro por {dia:0.0F} dia(s) e percorreu {km:0.2F} km.')
print(f' O valor total a pagar foi de: R${valor_total_dia:0.2f} (dia(s)) + R${valor_total_km:0.2f} (km) = R${valor_total_pagar:0.2f}.')
print('¬' * 80)
