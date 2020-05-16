# Desafio 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
'''
ex.:
Ana Maria de Souza
primeiro: Ana
último: Souza
'''

nome = str(input('Digite o seu nome completo: ')).strip().title()

nome_lista = nome.split()
nome_final = ' '.join(nome_lista)

print(f'Seu nome completo é {nome_final}, seu primeiro nome é {nome_lista[0]} e o último é {nome_lista[-1]}.')
# Resolução alternativa:
# para o último nome pode ser utilizada a função 'nome[len(nome)-1]', que também vai mostrar o nome que está na última posição.
