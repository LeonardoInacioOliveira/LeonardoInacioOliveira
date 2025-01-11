import statistics

empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900]

media1 = statistics.mean (empresa1)
mediana1 = statistics.median (empresa1)
moda1 = statistics.mode (empresa1)
desviopadrao1 = statistics.stdev(empresa1)
variancia1 = statistics.variance(empresa1)

media2 = statistics.mean (empresa2)
mediana2 = statistics.median (empresa2)
moda2 = statistics.mode (empresa2)
desviopadrao2 = statistics.stdev(empresa2)
variancia2 = statistics.variance(empresa2)

media3 = statistics.mean (empresa3)
mediana3 = statistics.median (empresa3)
moda3 = statistics.mode (empresa3)
desviopadrao3 = statistics.stdev(empresa3)
variancia3 = statistics.variance(empresa3)

media4 = statistics.mean (empresa4)
mediana4 = statistics.median (empresa4)
moda4 = statistics.mode (empresa4)
desviopadrao4 = statistics.stdev(empresa4)
variancia4 = statistics.variance(empresa4)

print('EMPRESA 1')
print('Salário Médio:', media1)
print('Mediana dos Salários:', mediana1)
print('Moda dos Salários:', moda1)
print('Desvio Padrão nos Salários:', desviopadrao1)
print('Variância nos Salários:', variancia1)

print()
print('EMPRESA 2')
print('Salário Médio:', media2)
print('Mediana dos Salários:', mediana2)
print('Moda dos Salários:', moda2)
print('Desvio Padrão nos Salários:', desviopadrao2)
print('Variância nos Salários:', variancia2)

print()
print('EMPRESA 2')
print('Salário Médio:', media3)
print('Mediana dos Salários:', mediana3)
print('Moda dos Salários:', moda3)
print('Desvio Padrão nos Salários:', desviopadrao3)
print('Variância nos Salários:', variancia3)

print()
print('EMPRESA 4')
print('Salário Médio:', media4)
print('Mediana dos Salários:', mediana4)
print('Moda dos Salários:', moda4)
print('Desvio Padrão nos Salários:', desviopadrao4)
print('Variância nos Salários:', variancia4)

#Eu escolho a Empresa 2, pois é a que o maior menor salário possível é o maior dentre todas, e também porque é ela a que tem o
#menor desvio padrão