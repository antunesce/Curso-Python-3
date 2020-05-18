# Cores no Terminal (ANSI).

"""
ANSI escape sequence
Sempre que quiser incluir uma cor no código Python utilizar o código:

\033[style; text; back_m

Style - é o estilo da fonte.
 0 - none (sem estilo)
 1 - bold (negrito)
 4 - underline (sublinhado)
 7 - inverte a configuração da cor da letra e do fundo.

Text / back -  é a cor do texto / fundo
 30  /  40  - branco
 31  /  41  - vermelho
 32  /  42  - verde
 33  /  43  - amarelo
 34  /  44  - azul
 35  /  45  - roxo
 36  /  46  - ciano
 37  /  47  - cinza

teste
 1 - \033[0:30:41m
 2 - \033[4:33:44m
 3 - \033[1:35:43m
 4 - \033[:30:42m # quando não é colocado o stylo é dado como padrão 'sem padrão'.
 5 - \033[m # retorna o padrão do terminal
 6 - \033[7:30m # inverte as cores do fundo e do texto
"""

a = 3
b = 5
print(f'Os valores são \033[1;35m{a}\033[m e \033[1;31m{b}\033[m !!!')
