# Desafio 014: Escreva um programa que converta uma temperatura digitada em °C e converta em °F.

#0 °C × 9/5) + 32

print('=' * 40)
print('  Conversor de temperatura (°C -> °F)')
print('=' * 40)
print('')
temp_celsius = float(input('Digite a temperatura em Celsius (°C):'))
print('')

temp_fahrenheit = (temp_celsius * (9/5)) + 32

print('-' * 40)
print(f'{temp_celsius}°C é igual a {temp_fahrenheit}°F.')
print('=' * 40)