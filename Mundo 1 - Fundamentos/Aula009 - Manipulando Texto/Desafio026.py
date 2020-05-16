# Desafio 026: Faça um programa que leia uma frase pelo teclado e mostre:

# 1. Quantas vezes aparece a letra "A".
frase = str(input('Digite uma frase: ')).strip().lower()

frase_lista = frase.split()
frase_final = ' '.join(frase_lista).capitalize()
frase_count_a = frase.count('a')
frase_find_a = frase.find('a')
frase_rfind_a = frase.rfind('a')

print(f'Você digitou "{frase_final}", possue(m) {frase_count_a} letra(s) "a".')

# 2. Em que posição ela aparece a primeira vez.
print(f'A letra "a" aparece a primeira vez na posição {frase_find_a + 1}.')

# 3. Em que posição ela aparece a última vez.
print(f'A letra "a" aparece a última vez na posição {frase_rfind_a + 1}.')