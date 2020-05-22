# Condições Aninhadas
'''
- tendo um bloco:
if carro.esqueda():
    bloco 1

- tendo dois blocos:
if casso.esqueda():
    bloco 1
else:
    bloco 2

- tendo 3 blocos
if carro.esquerda():
    bloco 1
elif carro.direita():
    bloco 2
else:
    bloco 3

- tendo quatro ou mais blocos
if carro.esquerda():
    bloco 1
elif carro.direita():
    bloco 2
elif carro.re():
    bloco 3
else:
    bloco 4

* Sempre começa com o if, nunca com o elif.
* Dentro do if pode-se utilizar quantas vezes quiser o elif:, porém o else utiliza uma vez ou nenhuma.
* elif só pode ser utilizado com if.
'''

nome = str(input('Digite seu nome: ')).strip().title()

if nome == 'Diego':
    print(f'Seu nome é muito bonito.')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'João':
    print(f'Legal seu nome é bíblico.')
elif nome in 'Ana Celia Celina Clara':
    print('Que belo nome.')
else:
    print('Seu nome é bem normal.')

print(f'Tenho um bom dia, {nome}!')
