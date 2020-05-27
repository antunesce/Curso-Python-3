# Desafio 042: Refaça o Desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
'''
- Equilátero : todos os lados são iguais
- Isósceles: dois lados iguais
- Escaleno: todos os lados são diferentes
'''

print('-' * 60)
print('{:^60}'.format('Testando triângulos v1.0'))
print('-' * 60)
l1 = float(input('Digite o lado 1 do triângulo: '))
l2 = float(input('Digite o lado 2 do triângulo: '))
l3 = float(input('Digite o lado 3 do triângulo: '))
print('-' * 60)
print('')

# Teste de formação do triângulo
if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    # Teste do tipo de triângulo
    if l1 == l2 == l3:
        print(f'O triângulo de lado {l1:0.1f}, {l2:0.1f} e {l3:0.1f} é um Equilátero.')
    elif l1 != l2 != l3 != l1:
        print(f'O triângulo de lado {l1:0.1f}, {l2:0.1f} e {l3:0.1f} é um Escaleno.')
    else:
        print(f'O triângulo de lado {l1:0.1f}, {l2:0.1f} e {l3:0.1f} é um Isósceles.')
else:
    print(f'Não é possível formar um triângulo com os lados {l1:0.1f}, {l2:0.1f} e {l3:0.1f}.')

print('')
print('-' * 60)