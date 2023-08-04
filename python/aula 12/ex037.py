'''Escreva um programa que leia um número inteiro qualquer e peça para
o usuário escolher qual será a base de conversão:
    - 1 para binário;
    - 2 para octal
    - 3 para hexadecimal'''

decimal = int(input('Digite um numero decimal:'))
conversao = int(input('Agora escolha converter para: 1-Binario, 2-Octal e 3-Hexadecimal'))

if conversao == 1:
    decimal = bin(decimal)
elif conversao == 2:
    decimal = oct(decimal)
elif conversao == 3:
    decimal = hex(decimal)
else:
    print('Voce tem que escolher entre o nº 1, 2 ou 3. Inicie o programa novamente.')

print(decimal)