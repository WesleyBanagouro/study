'''Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
Use a função len(string) para saber o tamanho de um texto (número de caracteres).'''


nome = input('Digite um nome: ').capitalize()
while len(nome) < 3:
    nome = input('Digite um nome com mais de 3 letras: ')

idade = int(input('Digite uma idade: '))
while idade < 0 or idade > 150:
    idade = int(input('Digite uma idade entre 0 e 150: '))

salario = float(input('Digite um salário: '))
while salario < 0:
    salario = float(input('Digite um salario maior do que 0: '))

sexo = input('Digite um sexo (M ou F): ').upper()
while sexo not in ['M', 'F']:
    sexo = input('Digite um sexo válido (M ou F): ').upper()

estado_civil = input('Digite um estado civil (S, C, V ou D): ').upper()
while estado_civil not in ['S', 'C', 'V', 'D']:
    estado_civil = input('Digite um estado civil válido:\n S: Solteiro\n C: Casado\n V: Viúvo\n D: Divorciado\n').upper()

print(nome)
print(idade)
print(salario)
print(sexo)
print(estado_civil)
