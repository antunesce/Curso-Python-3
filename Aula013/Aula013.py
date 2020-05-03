# Laços de repetição (parte 1)
"""
Laço com variável de controle

laço c no intervalo (1,10)
    se moeda
        pega
    passo
    pula
passo
pega

em Python:

for c in range(1,10):
    if moeda:
        pega
    passo
    pula
passo
pega

"""

'''for c in range(0, 6): # Ele vai contar de 0 a 5, porque quando chegar em 6 ele para e não printa.
    print(c)
print('FIM')'''

'''for c in range(1, 6):'''
# Nesse caso ele vai contar de 1 a 5, e parar no 6. Então ele sempre conta do primeiro número ao penúltimo do informado.

'''for c in range(6, 0, -1)'''
# invertendo os números, colocando o maior primeiro e o menor e acrescentando o -1 fará uma contagem regressiva.
# Ele vai mostrar o n° 6 e vai retirar 1, até chegar no 0 e parar a contagem, não irá mostrar o 0.

'''for c in range(0, 7, 2)'''
# Irá fazer uma contagem de 0 a 6, porque no 7 ele para e não mostra, e será feita esta contagem de 2 em 2.
# ou seja, o terceiro número colocado irá adicionar 2 à contagem.

# Fazendo um contador progressivo:
'''
inicio = int(input('Digitie o início da contagem: '))
fim = int(input('Digite o final da contagem: '))
passo = int(input('Digite o passo da contagem: '))

for c in range(inicio, fim + 1, passo):
    print(c)
print('FIM')'''

# Somador de números:
s = 0  # variável criada para armazenar os números que forem adicionados
for c in range(0, 3):  # o comando será repetido 3 vezes
    n = int(input('Digite um valor: '))  # este comando será executando 3 vezes, pedindo para informar um número
    s += n  # será adicionado à variável 's' o valor que for informado em n, esse comando será repetido 3x
print(f'O somatório de todos os números é {s}')  # apresentará o resultado da somatória dos 3 númros informados
