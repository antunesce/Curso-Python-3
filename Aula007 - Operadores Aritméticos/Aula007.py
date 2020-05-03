# Operadores Aritméticos
# + (Adição). obs.: ao utilizar o sinal de somar (+) com strings ele concatenará, ou seja, juntará os termos em string.
# ex.: 'oi' + 'oi' -> 'oioi'
# - (Subtração)
# * (Multiplicação). obs.: ao utilizar o sinal de multiplicar (*) com strings ele multiplicara a quantidade da mensagem.
# ex.: 'oi' * 5 -> 'oioioioioi'
# / (Divisão)
# ** (Potência) ou 'pow(x,y)', o 'x' é a base e o 'y' é o expoente.
# // (Divisão inteira)
# % (Módulo ou resto da divisão)

# Ordem de precedência
# 1- ()
# 2- **
# 3- * / // %
# 4- + -

# print(5 + 3 * 2 == 11)
# print(3 * 5 + 4 ** 2 == 31)
# print(243 == 3 * (5 + 4) ** 2)

#nome = input('Qual o seu nome? ')
#print(f'Muito prazer em te conhcer {nome:20}!') #:20 -> ':'permite que a variável 'nome' seja escrita em '20'caracteres.
#print(f'Muito prazer em te conhcer {nome:>20}!') #:>20 -> '>' permite que a variável 'nome' seja alinhada à esquerda.
#print(f'Muito prazer em te conhcer {nome:<20}!') #:<20 -> '<' permite que a variável 'nome' seja alinhada à direita.
#print(f'Muito prazer em te conhcer {nome:^20}!') #:^20 -> '^' permite que a variável 'nome' seja alinhada ao centro.
#print(f'Muito prazer em te conhcer {nome:=^20}!') #:=^20 -> '=' pode ser adicionado algum símbolo e ele será adicionado ao espaço determinado, nesse caso a '20' caracteres.

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
dm = n1 % n2
e = n1 ** n2
print('A soma é {}, a subtração é {} e a multiplicação é {}.'.format(s, sub, m), end=' ') #'end='' -> no final da linha ele não irá quebrar a linha ele juntará a linha de baixo. Entre as aspas ('') pode ser colocado qualquer simbolo.
print('A divisão é {:.3f}, a divisão inteira é {}, divisão em módulo é {}.'.format(d, di, dm)) #no caso da divisão utilizou-se '{:.3f}', onde: '.3' refere-se a quantidade de casas decimais e o 'f' para dizer que é um número flutuante.
print(f'A \n exponenciação \n é {e}.') #'\n' -> quebra a linha