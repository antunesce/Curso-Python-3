# Desafio 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = input('Digite o nome de uma cidade: ').lower().strip()

santo = 'santo' in cidade

print(f'A cidade que você digitou começa com "Santo"? {santo}.')
