'''
***Operadores Aritméticos***    
+ (Adição)
obs.: ao utilizar o sinal de somar (+) com strings ele concatenará, ou seja, juntará os termos em string.
ex.: 'oi' + 'oi' -> 'oioi'
- (Subtração)
* (Multiplicação)
obs.: ao utilizar o sinal de multiplicar (*) com strings ele multiplicara a quantidade da mensagem.
ex.: 'oi' * 5 -> 'oioioioioi'
/ (Divisão)
** (Potência) ou 'pow(x,y)', o 'x' é a base e o 'y' é o expoente.
// (Divisão inteira) - É o valor inteiro da divisão
% (Módulo ou resto da divisão) - É o resto da divisão

operando 
***Ordem de precedência***
1- ()
2- **
3- * / // %
4- + -

***Expressões Lógicas ***
== (igual)
!= (diferente)
> (maior que)
< (menor que)
>= (maior ou igual)
<= (menor ou igual)

Ex.:
5 + 3 * 2 -> dentre os operadores aritmétios a precedência é multiplicação (*) e depois a soma (+)
3 * 5 + 4 ** 2 -> dentre os operadores aritméticos a precedência é potência (**), multiplcação (*) e depois soma (+)
3 * (5 + 4) ** 2 -> dentre os operadores aritméticos a precedência é parentêse (), potência (**) e depois multiplicação (*)

***Alinhamento e tratamento de string***
nome = input('Qual o seu nome? ')
print(f'Muito prazer em te conhcer {nome:20}!') ':20' -> ':'permite que a variável 'nome' seja escrita em '20'caracteres.
print(f'Muito prazer em te conhcer {nome:>20}!') ':>20' -> '>' permite que a variável 'nome' seja alinhada à esquerda.
print(f'Muito prazer em te conhcer {nome:<20}!') ':<20' -> '<' permite que a variável 'nome' seja alinhada à direita.
print(f'Muito prazer em te conhcer {nome:^20}!') ':^20' -> '^' permite que a variável 'nome' seja alinhada ao centro.
print(f'Muito prazer em te conhcer {nome:=^20}!') ':=^20' -> '=' adicionará algum símbolo ao espaço restante de caracteres que foi determinado.
'''

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
dm = n1 % n2
e = n1 ** n2
print('A soma é {}, a subtração é {} e a multiplicação é {}.'.format(s, sub, m), end='') #'end=' -> não irá quebrar a linha, juntará a linha de baixo a esta. Entre as aspas ('') pode ser colocado qualquer simbolo.
print('A divisão é {:.3f}, a divisão inteira é {}, divisão em módulo é {}.'.format(d, di, dm)) #'{:.3f}', '.3' refere-se a quantidade de casas decimais e o 'f' significa que é um número flutuante.
print(f'A \n exponenciação \n é {e}.') #'\n' -> faz a quebra da linha
