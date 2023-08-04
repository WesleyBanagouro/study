# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random

aluno1 = str(input('Digite o primeiro aluno:'))
aluno2 = str(input('Digite o segundo aluno:'))
aluno3 = str(input('Digite o terceiro aluno:'))
aluno4 = str(input('Digite o quarto aluno:'))
lista_alunos = [aluno1, aluno2, aluno3, aluno4]
random.shuffle(lista_alunos)
print(lista_alunos)