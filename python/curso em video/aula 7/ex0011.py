# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pinta-la, sabendo que cada litro de tinta pinta uma área de 2m².
alt = float(input('Qual a altura da parede? '))
larg = float(input('Qual a largura da parede? '))
print('Considerando que a parede tem {}m de altura e {}m de largura, sua área sera de {}m², e será preciso {} litros de tinta para pintar a parede inteira!'.format(alt, larg, alt*larg, alt*larg/2))