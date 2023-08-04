'''Crie um programa que leia varios números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer continuar a digitar valores.'''

numeros = []
continuar = input('Vamos começar? ').capitalize().strip()

while continuar == 'Sim':
    add = int(input('Digite um numero: '))
    numeros.append(add)
    continuar = input('Quer continuar? ').capitalize().strip()

maior = max(numeros)
menor = min(numeros)
media = sum(numeros)/len(numeros)
print('A média dos valores digitados é igual a {}. O maior valor foi o {} e o menor foi o {}.'.format(media, maior, menor))