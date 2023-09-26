'''Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.'''

distancia = float(input('Qual a distância a ser percorrida? '))

if distancia > 200:
    valor = distancia * 0.45
    print('O Valor da viagem é de R$ {:.2f}'.format(valor))
else:
    valor = distancia * 0.50
    print('O Valor da viagem é de R$ {:.2f}'.format(valor))

