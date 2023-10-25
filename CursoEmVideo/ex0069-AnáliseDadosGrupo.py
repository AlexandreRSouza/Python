total_h = total_m = total_18 = 0
while True:
    idade = int(input('Digite sua idade. '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo,[M/F] ')).strip().upper()[0]
    if idade >= 18:
        total_18 += 1
    if sexo == 'M':
        total_h += 1
    if sexo == 'F' and idade < 20:
        total_m += 1
    continua = ' '
    while continua not in 'SN':
         continua = (input('Deseja Continuar? [S/N]')).strip().upper()[0]
    if continua == 'N':
        break
print(f'O Total de pessoas acima de 18 anos é de {total_18}')
print(f'O Total de Homens é de {total_h}')
print(f'O Total de Mulheres abaixo de 21 anos é de {total_m}')
print('ACABOU')




'''print(f'O Total de pessoas acima de 18 anos é de {total_18}')
print(f'O Total de Homens é de {total_h}')
print(f'O Total de Homens é de {total_m}')'''