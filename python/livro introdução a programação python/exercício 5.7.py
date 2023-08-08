'''n = int(input("Tabuada de:"))
x = 1
while x <= 10:
print(n*x)
 x=x*1

Exercício 5.7 Modifique o programa anterior de forma que o usuário também 
digite o início e o fim da tabuada, em vez de começar com 1 e 10.'''

n = int(input("Tabuada de:"))
inicio = int(input('Quer que comece de: '))
fim = int(input('E termine em: '))

while inicio <= fim:
    print('{} x {} = {}'.format(n, inicio, n * inicio))
    print('-' * 30)
    inicio += 1