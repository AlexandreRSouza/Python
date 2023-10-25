gasto = mais_mil = mais_barato = cont = 0
barato = ' '
while True:
    nome = str(input('Digite o nome do produto. '))
    preco = float(input('Digite o valor em R$ '))
    cont += 1
    gasto += preco
    if preco > 1000:
        mais_mil += 1
    if mais_barato < preco:
        mais_barato = preco
    #o bloco do comando IF pode ser resumido devido ser o mesmo comando e para executar utilizando o OR.
    if cont == 1 or preco < mais_barato:
        mais_barato = preco
        barato = nome
    #Abaixo o comando usando IF e ELSE:
    '''if cont == 1:
        mais_barato = preco
        barato = nome
    else:
        if preco < mais_barato:
            mais_barato = preco
            barato = nome'''
    continua = ' '
    while continua not in 'SN':
        continua = (input('Deseja Continuar? [S/N]')).strip().upper()[0] 
    if continua == 'N':
        break       
print(f'O total da compra foi de R$ {gasto:.2f}')
print(f'{mais_mil} produto(s) custou mais de R$ 1.000')
print(f'O produto mais barato é {nome} e custou R$ {mais_barato:.2f}')
print('ACABOU')






