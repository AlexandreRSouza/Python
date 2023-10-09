num = int(input('Digite um número inteiro: '))
total = 0
for c in range(1, num + 1):#aqui está fazendo uma contagem apartir do 1 até o número digitado.
    if num % c == 0:
        print('\033[33m', end=' ')#fica na cor amarelo os divisiveis
        total = total + 1 #contador para saber quantas vezes está sendo dividido
    else:
        print('\033[31m', end=' ')#fica na cor vermelho os não divisiveis
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divísivel {} vezes.'.format(num, total))
if total == 2:
    print('O número {} É PRIMO!'.format(num))
else:
    print('O Número {} NÃO É PRIMO.'.format(num))

