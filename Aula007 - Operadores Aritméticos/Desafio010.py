# Desafio 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Cotação do dólar no exercício => $ 1,00 = R$ 3,27

print('.' * 40)
print('CONVERSOR DE MOEDA')
print('.' * 40)
moeda = input('Você quer converter real para qual moeda? ')
cotacao = float(input(f'Qual a cotação do {moeda}? (ex.: 1.32) $ '))
valor = float(input(f'Qual o valor em reais a ser convertido em {moeda}? R$ '))

novo_valor = valor / cotacao

print(f'R${valor:0.2f} convertidos em {moeda} é igual a ${novo_valor:0.2f}.')
