# Condições Aninhadas
'''
tendo um bloco:
if carro.esqueda():
    bloco 1

tendo dois blocos:
if casso.esqueda():
    bloco 1
else:
    bloco 2

tendo 3 blocos
if carro.esquerda():
    bloco 1
elif carro.direita():
    bloco 2
else:
    bloco 3

tendo quatro ou mais blocos
if carro.esquerda():
    bloco 1
elif carro.direita():
    bloco 2
elif carro.re():
    bloco 3
else:
    bloco 4

* Dentro do if pode-se utilizar quantas vezes quiser o elif:, porém o else utiliza uma vez ou nenhuma.
* elif só pode ser utilizado com if.
'''

nome = str(input('Qual o seu nome? ')).title().strip()
if nome == 'Diego':
    print('Que nome bonito!')
elif nome == 'João' or nome == 'Maria' or nome == 'Francisco':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'Ana Claudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print(f'Tenha um bom dia {nome}.')
