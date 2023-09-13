km = float(input('Quantos Km percorrido '))
dia = int(input('Quantod dias de aluguel? '))

aluguel_dia = 60 * dia
aluguel_km = 0.15 * km
total = aluguel_km + aluguel_dia

print('O valor a pagar pelo aluguel do carro é de R$ {:.2f}' .format(total))