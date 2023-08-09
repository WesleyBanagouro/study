frase = '      Essa é uma frase aleatoriamente aleatoria de forma aleatoria.     '
print(frase[2:7]) # Pega um intervalo dentro da string
print(frase[2:21:2]) # Pega um intervalo e depois salta 2 caracteres
print(frase[:10]) # Começa do caracter 0
print(frase[10:]) # Pega toda a string a partir do caracter 10
print(frase[10::2]) # Começa a partir do 10, vai até o final e pula de 2 em 2
print(len(frase)) # Retorna qual o comprimento da string
print(frase.count('a')) # Conta quantos 'a' tem na string
print(frase.count('a', 0, 13)) # Conta quantos 'a' tem no intervalo de 0 a 13 na string
print(frase.find('ale')) # Mostra onde começa a sequencia 'ale' na string
print('frase' in frase) # Procura 'frase' na variável frase
print(frase.replace('frase', 'texto')) # Troca 'frase' por 'texto'
print(frase.upper()) # Deixa maiuscula
print(frase.lower()) # Deixa minuscula
print(frase.capitalize()) # Somente a inicial como maiuscula
print(frase.title()) # Deixa cada palavra maiuscula
print(frase.strip()) # Retira espaços inúteis
print(frase.rstrip()) # Retira espaços inúteis somente da direita.
print(frase.split()) # Separa onde houver espaço (padrão)
print(frase.split('a')) # Separa onde houver 'a'



