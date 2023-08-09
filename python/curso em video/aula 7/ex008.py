# Escreva um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.
m = int(input('Digite um valor em metros: '))
print('O valor {}m em centimetros vale {}cm, em milimetros vale {}mm!'.format(m, m*100, m*1000))