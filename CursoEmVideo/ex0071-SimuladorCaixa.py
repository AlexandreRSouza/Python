print('='*30)
print('{:^30}'.format('BANCO X'))
print('='*30)

sacar = int(input('Qual valor a ser Sacado em R$ '))
total = sacar#variavel está recebcendo o valor a ser casado
ced = 50#iniciciou a variavel cédula no valor de 50 reais
totalced = 0#total de cédulas 

while True:    
    if total >= ced:
        total -= ced
        totalced += 1
    else:
        if totalced > 0:
            print(f'Recebu {totalced} notas de R$ {ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break
print('='*30)
print('{:^30}'.format('Volte Sempre ! BANCO X'))
print('='*30)


