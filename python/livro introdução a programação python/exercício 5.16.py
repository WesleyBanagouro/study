'''Exercício 5.16 Execute o programa (Listagem 5.14) para os seguintes valores: 501,
745, 384, 2, 7 e 1.'''

contador = 0
soma = 0

while True:
    numero = int(input('Digite um número ou 0 para finalizar: '))
    if numero == 0:
        break
    contador += 1
    soma += numero
print(f'Você digitou {contador} números, a soma entre eles é {soma} e a média aritmetica é {soma / contador}.')