#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Qual seu salário R$ '))

if salario <= 1250:
    novo_salario = salario + (salario * 15 / 100)
else:
    novo_salario = salario + (salario * 10 / 100)
print('Seu salário é de R$ {} e com aumento foi para R$ {}.' .format(salario, novo_salario))