#convertendo tipos 

#int p/ float e float para int
preco = 10 #int
preco = float(preco) #float
print(preco) #saída


#convertendo de int p float por divisão 
preco = 10 
print (preco / 2) # de int p/ float
print(preco //2) # de float p int 


#númerico para string - ou seja,  pega o constrututor e passa o valor do tipo de dado nele 
preco = 10.50
idade = 28
print(str(preco)) 
print(str(idade))

#concatenar str com variaveis - f é utilizado como string e você passa variaveis dentro da mesma
texto = f"idade {idade} preco {preco}"
print(texto) 

#string para númerico 
preco = "10.50"
idade = "20"
print(float(preco))

###################################################################################################################################
#+ exemplos 

print(int(1.9)) #float para inteiro 

print(int("10")) # de str para int, base 10

print(float("10.10")) # de str para float

valor = 10
valor_str = str(valor)
print(type(valor))
print(type(str(10.10))) #type identifica o tipo de variavel enquanto converte 

