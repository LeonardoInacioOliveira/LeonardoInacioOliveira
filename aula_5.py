#EXERCÍCIOS

#1 - Imprima uma mensagem de boas-vindas na tela.
print("EXERCÍCIO 1")
nome = input("Digite o seu nome: ")
bienvenue = "Seja bem-vindo(a),"
print(bienvenue,nome+'!')

#2 - Declare uma variável booleana verdadeiro com o valor True e imprima seu tipo
print("\nEXERCÍCIO 2")
verdadeiro = True
tipo = type(verdadeiro)
print(tipo)

#3 -  Imprima o resultado da multiplicação de dois números decimais de sua escolha
print("\nEXERCÍCIO 3")
fator1 = 5.5
fator2 = 6.5
produto = fator1*fator2
print(produto)

#4 - Imprima o resultado da divisão de dois números inteiros de sua escolha
print("\nEXERCÍCIO 4")
dividendo = 23
divisor = 41
cociente = dividendo/divisor
print(cociente)

#5 - Imprima o resultado da subtração de dois números inteiros de sua escolha
print("\nEXERCÍCIO 5")
subtraendo = 9 
minuendo = 21
diferenca = subtraendo-minuendo
print(diferenca)

#6 - Imprima o resultado da divisão inteira de dois números inteiros de sua escolha
print("\nEXERCÍCIO 6")
dividendo = 23
divisor = 41
cociente = dividendo/divisor
cociente_int = int(cociente)
print(cociente_int)

#7 - Imprima o resultado da multiplicação de 4 números decimais de sua escolha
print("\nEXERCÍCIO 7")
fator1 = 25.4
fator2 = 50.8
fator3 = 12.7
fator4 = 19.05
produtozao = fator1*fator2*fator3*fator4
print(produtozao)

#8 - Declare uma variável numero e atribua um número inteiro. Em seguida, imprima o dobro desse número
print("\nEXERCÍCIO 8")
numero = 7
dobro = numero + numero
print(dobro)
 
 #9 - Crie uma calculadora de soma com as ferramentas que vc já conhece (Use apenas input, print e variavel)
print("\nEXERCÍCIO 9")
x = float(input("Digite um número: "))
y = float(input("Digite um outro número: "))
soma = x+y
difference = x-y
product = x*y
quociente = x/y
print(soma)
print(difference)
print(product)
print(quociente)

#10 - Crie um sistema de cadastro com as estruturas que vc já conhece (Use apenas input, print e variavel)
print("\nEXERCÍCIO 10")
nome = input("Digite o seu nome: ")
email = input("Digite o seu e-mail: ")
senha = input("Digite a sua senha: ")
print("NOME:",nome,"|| E-MAIL:",email,"|| SENHA:",senha)
print("Agora que as informações estão devidamente preenchidas, podeis aceder ao nosso site!")