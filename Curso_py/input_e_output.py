#input
""" input é utilizado quando queremos ler dados da entrada do teclado, então, quando ela recebe um argumento do tipo string, a 
função lê a entrada, converte para string e retorna o valor na tela do usuário"""

#exemplo
#nome = input("Informe o seu nome:")

#exibindo valor com print
""" o print é utilizado quando queremos exibir dados, ela recebe um argumento obrigatório do tipo de varargs de objetos e 4 
argumentos opcionais (sep, end, file e flush). Todos os objetos são convertidos para str, seprados por sep e terminados por end"""

#exemplos 
nome = "Guilherme"
sobrenome = "Carvalho"

print(nome, sobrenome)
print(nome, sobrenome, end="...\n") #parametro para terminar com o txt e quebra de linha
print(nome, sobrenome, sep="#") #utilizado para preencher o espaço vazio

#####################################################################################################################
#exemplos

nome = input("Informe o seu nome:")
idade = input("Informe a sua idade:")

print(nome, idade, end="...\n")



