# Desafio 024: Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".

cidade = str(input('Digite o nome de uma cidade: ')).lower().strip()

santo = 'santo' in cidade # Melhor forma, porque no input já tem as funções '.lower()' e '.strip()'.
# Resolução alternativa 'cidade[0:5] == 'Santo''. Contudo, caso o usuário digite em minúsculo ou maiúsculo vai dar errado.

print(f'A cidade que você digitou começa com "Santo"? {santo}.')
