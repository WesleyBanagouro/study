'''
fim=int(input("Digite o último número a imprimir:"))
x = 0
while x <= fim:
print(x)
 x = x + 2

Exercício 5.5 Reescreva o programa anterior para escrever os 10 primeiros múltiplos de 3.'''

multiplo = int(input("Multiplo de qual número:"))
numero = 0

while numero < 10:
    print(multiplo * numero)
    numero += 1