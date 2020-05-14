'''
*** Estrutura sequencial ***
Até o momento todos os scripts que foram escritos foram feitos seguindo uma estrutura sequencial.
Essas estruturas sequênciais são estruturas que seguem uma sequência de passos, onde todos os passos são executados, caso algum desses passos sejam modificados o resultado poderá ser modificado ou a sequência pode ser quebrada, inviabilizando o correto funcinoamento do script.

*** Condições simples e compostas (parte 1) ***

1) Representação de uma estrutura condicional
- simples:
if conditional

- composta:
if conditional:
    True block
else:
    False block
#nunca será executa o bloco True e o bloco False ao mesmo tempo, ou é um, ou o outro.

ex.1:
tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('Seu carro é novo')
else:
    print('Eita carro véi!!!')

print('----- FIM!!! -----')

- condicional simplificada
ex.2:
print('Carro novo' if tempo <=3 else 'Carro velho')

ex.3:
nome = str(input('Digite seu nome: '))

if nome == 'Diego':
    print('Que nome bonito você tem!')
else:
    print('Seu nome é tão normal.')
print(f'Bom dia {nome}!')
'''

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

media = (n1 + n2) / 2

print(f'A sua nota média é {media:0.1f}.')
if media >= 7.0:
    print('Sua média foi boa.')
else:
    print('Sua média foi ruim.')
