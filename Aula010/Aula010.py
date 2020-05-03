#Condições simples e compostas (parte 1)

'''
- Representação de uma estrutura condicional
if condição:
    bloco True
else:
    bloco False
*nunca será executa o bloco True e o bloco False ao mesmo tempo, ou é um, ou o outro.

ex:
tempo = int(input('Quantos anos tem seu carro? '))
if tempo <=3:
    print('Carro novo')
else:
    print('Carro velho')
print('----FIM----')

*Condição simplificada
print('Carro novo' if tempo <=3 else 'Carro velho')

ex2:
nome = str(input('Qual o seu nome? ')).title().strip()
if nome == 'Diego':
    print('Que nome bonito!')
else:
    print('Você tem um nome tão normal!')
print(f'Bom dia, {nome}.') '''

n1 = float(input('Digite a sua PRIMEIRA nota: '))
n2 = float(input('Digite a sua SEGUNDA nota: '))
m = (n1 + n2) / 2
if m >= 6:
    print('Parabéns, sua média foi boa.')
else:
    print('Sua média foi ruim. Estude mais!')
