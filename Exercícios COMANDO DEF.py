#EXERCÍCIOS AULA 10 - FUNÇÕES
print('''EXERCÍCIO 1'''
      )
def tipo_numero():
    n = float(input('Digite um número: '))
    if n % 2 == 0:
        print('Você digitou um número par.')
    else:
        print('Você digitou um número ímpar.')

tipo_numero()
print()

print('''EXERCÍCIO 2'''
      )
def multiplicar_tres_vezes():
    pila = float(input('Digite um número: '))
    dupla = float(input('Digite mais um número: '))
    trinca = float(input('Digite mais um: '))
    print(pila*dupla*trinca)

multiplicar_tres_vezes()
print()

print('''EXERCÍCIO 3'''
      )
def potencia():
    base = float(input('Digite o número a ser elevado: '))
    expoente = float(input('Digite o expoente: '))
    print(base**expoente)

potencia()
print()

print('''EXERCÍCIO 4'''
      )
def conselho():
    age = int(input('Digite a sua idade: '))
    if age == 18:
        print('Cuidado para não ser preso, moleque!')
    else:
        pass
        
conselho()
print()

print('''EXERCÍCIO 5'''
      )
def adivinhar_idade():
    age = int(input('Digite a sua idade: '))
    print('Você tem',age,'anos!')
    
adivinhar_idade()
print()

print('''EXERCÍCIO 6'''
      )
def copa_do_mundo():
    year = int(input('''ANOS DE COPA:
    1930
    1934
    1938
    1950
    1954
    1958
    1962
    1966
    1970
    1974
    1978
    1982
    1986
    1990
    1994
    1998
    2002
    2006
    2010
    2014
    2018
    2022.: '''))
    if year == 1930 or year == 1950:
        print('O Uruguai foi o campeão desta copa!')
    elif year == 1934 or year == 1938 or year == 1982 or year == 2006:
        print('A Itália foi a campeã desta copa!')
    elif year == 1954 or year == 1974 or year == 1990 or year == 2014:
        print('A Alemanha foi a campeã desta copa!')
    elif year == 1958 or year == 1962 or year == 1970 or year == 1994 or year == 2002:
        print('O Brasil foi o campeão desta copa!')
    elif year == 1966:
        print('A Inglaterra foi a campeã desta copa!')
    elif year == 1978 or year == 1986 or year == 2022:
        print('A Argentina foi a campeã desta copa!')
    elif year == 1998 or year == 2018:
        print('A França foi a campeã desta copa!')
    elif year == 2010:
        print('A Espanha foi a campeã desta copa!')
    elif year > 2022 and year % 4 == 2:
        print('Esta copa do mundo ainda não aconteceu!')
    else:
        print('Essa copa do mundo não existiu(existirá)!')
        
copa_do_mundo()

print()

print('''EXERCÍCIO 7'''
      )
def restaurante():
    option = int(input('''CARDÁPIO
1. Salada Tradicional - R$12,00
2. Macarronada à Bolonhesa - R$20,00
3. Sanduíche de Presunto - R$10,00
4. Sorvete de Chocolate - R$08,00: '''))
    if option == 1:
        print('Você optou pela Salada Tradicional - R$12,00!')
    elif option == 2:
        print('Você optou pela Macarronada à Bolonhesa - R$20,00!')
    elif option == 3:
        print('Você optou pelo Sanduíche de Presunto - R$10,00!')
    elif option == 4:
        print('Você optou pelo Sorvete de Chocolate - R$08,00!')
    else:
        repeat()
        
restaurante()