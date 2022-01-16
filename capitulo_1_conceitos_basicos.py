#Printar na tela
print('Hello world')

#Tipos de váriaveis

variavel_tipo_string = 'Conjunto de caracteres alfanumericos'


variavel_tipo_int = 12	# Número inteiro

variavel_tipo_float = 15.3 	# Número com casas decimais

variavel_tipo_bool = True	# Booleano

variavel_tipo_lista = [1, 2, 'Paulo', 'Maria', True]


variavel_tipo_dicionario = {'nome':'Felipe', 'idade':31}

variavel_tipo_tupla = ('Felipe', 'Ana', 3)

variavel_tipo_comentario = """Um comentário atribuido a uma variavel deixa de ser apenas um comentário, vira frase!!!"""

nome, idade, sexo, altura = 'Maria', 32, 'F', 1.89

#função input
nome = input('Digite seu nome: ')
print('Olá: ', nome)

#print usando mascara de substituição
print('Seja bem vindo(a) {}!!!'.format(nome))

#print avançado --> usando de f' strings
print(f'Seja bem vindo (a) {nome}, :)')
