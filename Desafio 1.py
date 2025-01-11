import statistics

alunos = []
notas = []
i = int(input('Digite, em algarismos, o número de alunos da classe: '))
print()
for nota in range (i):
    aluno = input('Digite o nome do aluno: ')
    alunos.append(aluno)
    nota = float(input('Digite a nota final do aluno: '))
    print()
    if nota > 10 or nota < 0:
        nota = float(input('Digite, novamente, a nota final do aluno: '))
        print()
        notas += [nota]
    else:
        notas += [nota]
        
print()
print(alunos)
print(notas)

mean = statistics.mean(notas)
mode = statistics.mode(notas) 
stdev = statistics.stdev(notas)
maximum = max(notas)
minimum = min(notas)

print()
print('Nota Média da Sala:',mean)
print('Moda das Notas da Sala:',mode)
print('Desvio Padrão das Notas da Sala:',stdev)
print('A maior nota foi',maximum)
print('A menor nota foi',minimum)

