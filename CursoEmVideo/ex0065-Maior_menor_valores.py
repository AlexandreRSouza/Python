num = 0
pergunta = ''
total = media = dig = 0
lista_num = []
menor = 0
maior = 0

while pergunta in 'SIM':
    num = int(input('Digite um número. '))
    total += num
    dig += 1
    media = total / dig  
    #lista_num.append(num)
    if dig == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    pergunta = input('''Deseja digitar mais valores: 
                                    [SIM] - Continua
                                    [NÃO] - Parar ''').upper()
#print('O maior número {} e menor número {} '.format(max(lista_num), min(lista_num)))
print('O Maior número é {} e o menor é {} '.format(maior, menor))
print('Você digitou {} e somou um total de {}'.format(dig, total))
print('A média foi de {}'.format(media))
print('FIM')
















