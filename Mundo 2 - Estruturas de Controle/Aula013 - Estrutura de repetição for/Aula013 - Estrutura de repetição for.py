# Laços de repetição (parte 1)
'''
*** Laço com variável de controle ***

laço c no intervalo(1,10) # c é a variável de controle. (1,10) é o intervalo de repetição, de 1 a 10.
    passo # o comando que irá ser executado dentro do intervalo 1, 10
pega # é o comando que será executado após a sequância (1, 10) terminar.

in python: # estrutura no python
for c in range(1, 10):
    passo
pega

*** Situações ***
1)
laço c no intervalo(0, 3)
    passo
    pula
passo
pega

for c in range(0, 3):
    passo
    pula
passo
pega

2)
laço c no intervalo(1,10)
    se moeda
        pega
    passo
    pula
passo
pega

in Python:
for c in range(1,10):
    if moeda:
        pega
    passo
    pula
passo
pega

# Exercício
# Se eu quisesse escrever 'Oi' 1000 vezes iria dar muito trabalho.
print('oi')
print('oi')
print('oi')
print('oi')
print('oi')
print('oi')

# Similar, poderia utilizar o laço de repetição

for c in range(1, 6): # A contagem é feita pela diferença entre o último número do intervalo e o primeiro número do intervalo (6 - 1 = 5), desta forma, será repetido 5x.
    print('oi')
print('FIM!')

for c in range(0, 6): # Ele vai contar de 0 a 5, porque quando chegar em 6 ele para e não printa.
    print(c)
print('FIM')

for c in range(1, 6): # Nesse caso ele vai contar de 1 a 5, e parar no 6. Então ele sempre conta do primeiro número ao penúltimo do informado.

for c in range(6, 0, -1): # invertendo os números, colocando o maior primeiro e o menor e acrescentando o -1 fará uma contagem regressiva.
    print(c) # Ele vai mostrar o n° 6 e vai retirar 1, até chegar no 0 e parar a contagem, não irá mostrar o 0.
print('FIM')

for c in range(0, 7, 2): # Irá fazer uma contagem de 0 a 6, porque no 7 ele para e não mostra, e será feita esta contagem de 2 em 2.
    print(c) # ou seja, o terceiro número colocado (x, x, 2) irá adicionar 2 à contagem.
print('FIM')

n = int(input('Digite um número: '))
for c in range(0, n + 1): # É possível ler um valor (n) e utilizar esse valor (n) para fazer parte do intervalo no for.
    print(c)
print('FIM')

# Fazendo um contador progressivo:

inicio = int(input('Digitie o início da contagem: '))
fim = int(input('Digite o final da contagem: '))
passo = int(input('Digite o passo da contagem: '))

for c in range(inicio, fim + 1, passo):
    print(c)
print('FIM')

Nessa situação seguiria a seguinte lógica:
A contagem vai iniciar pelo número informado na variável "inicio", até chegar ao final da contagem do valor atribuído a variável "fim", pulando números conforme a variável "passo".
Em uma situação hipotética, se as variáveis recebessem:
inicio = 1
fim = 10
passo = 2
A contagem se daria da seguinte forma:
primeiro valor = inicio = 1
segundo valor = inicio + passo = 1 + 2 = 3
terceiro valor = segundo valor + passo = 3 + 2 = 5
quarto valor = terceiro valor + passo = 5 + 2 = 7
quinto valor = quarto valor + passo = 7 + 2 = 9
sexto valor = quinto valor + passo = 9 + 2 = 11 *Nesse caso não iria ser printado, pois ultrapassa o valor atribuido na variável fim, que é 10

a sequência printada seria:
1
3
5
7
9
FIM

for c in range(0 , 3):
    n = int(input('Digite um número:')) # A estrutura do input está dentro de um for que tem um intervalo (0, 3), desta forma vai ser solicitado que se adicione um valor 3 vezes (3 - 0).
print('FIM')

# Somador de números:
s = 0  # variável criada para armazenar os números que forem adicionados
for c in range(0, 3):  # o comando será repetido 3 vezes (3 - 0 = 3), ou seja, a repetição acaba no número anterior ao último número informado no intervalo.
    n = int(input('Digite um valor: '))  # este comando será executando 3 vezes, pedindo para informar um número
    s += n  # será adicionado à variável 's' o valor que for informado em n, esse comando será repetido 3 vezes
print(f'O somatório de todos os números é {s}')  # apresentará o resultado da somatória dos 3 númros informados
'''
