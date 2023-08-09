'''Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.'''

user = input('Digite um usuario: ').capitalize()
password = input('Digite uma senha: ').capitalize()

while user == password:
    print('A senha não pode ser igual ao usuário.')
    password = input('Digite outra senha: ').capitalize()

print('Parabéns, você criou seu cadastro.')
print('Usuario: ', user)
print('Senha: ', password)