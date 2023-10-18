from time import sleep
opcao = 0
somar = 0
multiplicar = maior = novos_numeros = 0


num01 = int(input('Digite um valor. '))
num02 = int(input('Digite um valor. '))

while opcao != 5:
    print('''
            [1] - SOMAR
            [2] - MULTIPLICAR
            [3] - MAIOR
            [4] - NOVOS NÚMEROS
            [5] - SAIR''')
    opcao = int(input('Digite a opção desejada: '))

    if opcao == 1:
        somar = num01 + num02
        print('A soma dos dois valores é de {}'.format(somar))
    elif opcao == 2:
        multiplicar = num01 * num02
        print('A Multiplicação dos dois valores é de {}'.format(multiplicar))
    elif opcao == 3:
        if num01 > num02:
            print('O Maior valor é de {}'.format(num01))
        else:
            print('O Maior valor é de {}'.format(num02))
    elif opcao == 4:
        num01 = int(input('Digite um valor. '))
        num02 = int(input('Digite um valor. '))
    elif opcao == 5:
        print('Finalizando serviço....')
    else:
        print('Opção Inválida! Tente novamente. ')
    print('=-='*10)
    sleep(2)
print('SERVIÇO ENCERRADO!')