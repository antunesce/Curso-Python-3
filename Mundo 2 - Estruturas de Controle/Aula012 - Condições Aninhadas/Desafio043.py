# Desafio 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
'''
- Abaixo de 18.5: Abaixo do peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
'''

print('-' * 60)
print('{:^60}'.format('Calculadora de IMC v1.0'))
print('-' * 60)
peso = float(input('Qual o seu peso (kg): '))
altura = float(input('Qual a sua altura (m): '))
print('-' * 60)
print('')

imc = peso / (altura * altura)

if imc < 18.5:
    print(f'O seu IMC é de {imc:0.1f}, você está abaixo do peso.')
elif imc == 18.5 or imc <= 25:
    print(f'O seu IMC é de {imc:0.1f}, você está com o Peso ideal.')
elif imc == 25 or imc <= 30:
    print(f'O seu IMC é de {imc:0.1f}, você está com Sobrepeso.')
elif imc == 30 or imc <= 40:
    print(f'O seu IMC é de {imc:0.1f}, você está com Obesidade.')
else:
    print(f'O seum IMC é de {imc:0.1f}, você está com Obesidade morbida.')
print('')
print('-' * 60)
