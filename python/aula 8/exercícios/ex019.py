# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
alunos = 'Wesley', 'Pedro', 'João', 'Guilherme'
apagar = random.choice(alunos)
print('Quem irá apagar a lousa é o {}.'.format(apagar))
