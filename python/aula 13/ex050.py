'''Desenvolva um programa que leia seis números inteiros
e mostre a soma apenas daqueles que forem pares. Se o valor
digitado for ímpar, desconsidere-o'''

primeiro = 0  # Variável para armazenar o primeiro número digitado
ultimo = 0  # Variável para armazenar o último número digitado
soma = 0  # Variável para acumular a soma dos números pares

for c in range(0, 6):
    r = int(input('Digite um número:'))
    if c == 0:
        primeiro = r  # Atribui o primeiro valor digitado à variável primeiro
    if r % 2 == 0:
        soma += r
    ultimo = r  # Atualiza a variável ultimo em cada iteração

print('A soma dos números pares de {} a {} é igual a {}'.format(primeiro, ultimo, soma))


