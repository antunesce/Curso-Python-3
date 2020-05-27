# Desafio 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando no final, de acordo com a média atingida:
'''
- Média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- Média 7.0 ou superior: Aprovado
'''

print('-' * 60)
print('{:^60}'.format('Boletim escolar v1.0'))
print('-' * 60)
n1 = float(input('Digite a nota da primeira avaliação: '))
n2 = float(input('Digite a nota da segunda avaliação: '))
print('-' * 60)
print('')

media = (n1 + n2) / 2

if media < 5:
    print(f'A Média foi {media:0.1f}, \033[1;31mREPROVADO\033[m.')
elif media >= 7:
    print(f'A média foi {media:0.1f}, \033[1;32mAPROVADO\033[m.')
else:
    print(f'A média foi {media:0.1f}, \033[1;33mRECUPERAÇÃO\033[m.')

print('')
print('-' * 60)
