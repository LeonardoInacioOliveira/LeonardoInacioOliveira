'''- ***Desafio 2:  Condicionais***

***Sistema de Reservas de Hotel:***

***Você foi contratado(a) para desenvolver uma parte do sistema de um hotel. O objetivo é criar um sistema que gerencie reservas de quartos e o pagamento das diárias***.

- *Cadastro de Cliente:*

*O sistema deve permitir que o usuário "cadastre" o nome e a idade de até 3 clientes.*

- *Reservas de Quartos:*

***O sistema deve oferecer 3 tipos de quartos:*** 

***"Simples", "Duplo" e "Luxo".***

***Cada cliente deve escolher um quarto para sua estadia.
O preço da diária varia conforme o tipo de quarto:
Simples: R$ 100,00 por dia.
Duplo: R$ 150,00 por dia.
Luxo: R$ 250,00 por dia.***

- ***Cálculo da Estadia:***

***O usuário deve informar quantos dias cada cliente ficará no hotel.
O sistema deve calcular o valor total da estadia para cada cliente, considerando o tipo de quarto e a quantidade de dias.***

Exemplo: 

 ***valor_cliente3 = preco_duplo * cliente3_dias***

*Pagamento:*

*O sistema deve exibir o valor total a ser pago por cada cliente após a aplicação do desconto.*

*Regras Adicionais:
Utilize apenas variáveis, condicionais (if, elif, else) e listas para resolver o desafio.*

***O sistema não deve usar loops (for, while) nem funções.**
O código deve considerar todos os casos possíveis de escolha dos clientes.*'''

print("PRIMEIRO CADASTRO")
nome1 = input("Digite o nome: ")
idade1 = int(input("Digite a idade: "))
day1 = int(input("Por quantos dias vai ficar aqui?"))
op1 = int(input('''Escolha o tipo de quarto:
1. Simples - R$100,00 por dia.
2. Duplo - R$150,00 por dia.
3. Luxo - R$200,00 por dia.: '''))
if op1 == 1:
    value1 = 100*day1
    print("VALOR TOTAL =",value1,"reais")
elif op1 == 2:
    value1 = 150*day1
    print("VALOR TOTAL =",value1,"reais")
elif op1 == 3:
    value1 = 200*day1
    print("VALOR TOTAL =",value1,"reais")
else:
    quit()
    
print("SEGUNDO CADASTRO")
nome2 = input("Digite o nome: ")
idade2 = int(input("Digite a idade: "))
day2 = int(input("Por quantos dias vai ficar aqui?"))
op2 = int(input('''Escolha o tipo de quarto:
1. Simples - R$100,00 por dia.
2. Duplo - R$150,00 por dia.
3. Luxo - R$200,00 por dia.: '''))
if op2 == 1:
    value2 = 100*day2
    print("VALOR TOTAL =",value2,"reais")
elif op2 == 2:
    value2 = 150*day2
    print("VALOR TOTAL =",value2,"reais")
elif op2 == 3:
    value2 = 200*day2
    print("VALOR TOTAL =",value2,"reais")
else:
    quit()
print("TERCEIRO CADASTRO")
nome3 = input("Digite o nome: ")
idade3 = int(input("Digite a idade: "))
day3 = int(input("Por quantos dias vai ficar aqui?"))
op3 = int(input('''Escolha o tipo de quarto:
1. Simples - R$100,00 por dia.
2. Duplo - R$150,00 por dia.
3. Luxo - R$200,00 por dia.: '''))
if op3 == 1:
    value3 = 100*day3
    print("VALOR TOTAL =",value3,"reais")
elif op3 == 2:
    value3 = 150*day3
    print("VALOR TOTAL =",value3,"reais")
elif op3 == 3:
    value3 = 200*day3
    print("VALOR TOTAL =",value3,"reais")
else:
    quit()
    
cliente1 = [nome1, idade1, day1]
cliente2 = [nome2, idade2, day2]
cliente3 = [nome3, idade3, day3]
print(cliente1)
print(cliente2)
print(cliente3)






