dias = int(input('Quantos dias de aluguel? '))
km = float(input("Quantos KM rodados? "))
aluguel = dias * 60
km_total = 0.15 * km
total = aluguel + km_total
print('O quantidade de dias alugados é de {} dia e foi rodado {} km, sendo o valor total é de R$ {:.2f} a ser pago' .format(dias, km, total))

