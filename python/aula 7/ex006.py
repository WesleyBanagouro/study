# Solicita ao usuário que insira um número
num = float(input('Digite um número aqui: '))

# Calcula o dobro, triplo e a raiz quadrada do número
dobro = 2 * num
triplo = 3 * num
raiz_quadrada = num ** 0.5

# Exibe os resultados
print('O dobro do número {} é {:.2f}, o triplo vale {:.2f} e sua raiz quadrada é {:.3f}.'.format(num, dobro, triplo, raiz_quadrada))
