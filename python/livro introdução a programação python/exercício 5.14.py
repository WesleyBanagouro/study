'''Exercício 5.14 Escreva um programa que leia números inteiros do teclado. O programa deve ler os números até que o usuário digite 0 (zero). No final da execução, 
exiba a quantidade de números digitados, assim como a soma e a média aritmética.'''

contador = 0
soma = 0

while True:
    numero = int(input('Digite um número ou 0 para finalizar: '))
    if numero == 0:
        break
    contador += 1
    soma += numero
print(f'Você digitou {contador} números, a soma entre eles é {soma} e a média aritmetica é {soma / contador}.')