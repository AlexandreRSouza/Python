#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

valor_casa = float(input('Qual valor do imóvel? R$ '))
salario = float(input('Qual sua renda? R$ '))
finaciamento = int(input('Em qual tempo de financiamento? '))

prestacao = valor_casa / (finaciamento * 12)

por_salario = salario * 30 / 100


print('O Valor do Imóvel é de R$ {:.2f}\n Seu finaciamento é de {} anos\n O valor da prestação é de {:.2f}'.format(valor_casa, finaciamento, prestacao))

if prestacao > por_salario:
    print('\033[31;41m Seu financiamento foi negado, excedeu 30% da sua renda! que é de R$ {:.2f}\033[m'.format(por_salario))
else:
    print('=' * 50)
    print('\033[32;42mParabéns, Aprovado seu Financiamento\033[m')
   

