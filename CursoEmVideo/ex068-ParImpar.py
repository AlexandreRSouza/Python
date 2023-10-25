from random import randint, choice
soma = venceu = 0
while True:
    jogador = int(input('Jogue um número de 0 a 10. '))
    pc_gamer_num = randint(0,10)
    soma = jogador + pc_gamer_num
    opcao = ' '
    while opcao not in 'PI':
        opcao = input('Escolha PAR ou ÍMPAR [P / I]. ').strip().upper()[0]
    print(f'Você Jogou {jogador} e o PC jogou {pc_gamer_num}, ',end='')
    print('Deu PAR' if soma % 2 == 0 else 'Deu ÍMPAR')
    if opcao == 'P':
        if soma % 2 == 0:
            print('Você Venceu!!!!')
            venceu += 1
        else:
            print('Você Perdeu!!!!')
            break
    elif opcao == 'I':
        if soma % 2 == 1:
            print('Você Venceu!!!!')
            venceu += 1
        else:
            print('Você Perdeu!!!!')
            break
    print('Vamos Jogar Novamente! ')
print('GAME OVER!!!')
print(f'Você venceu {venceu} vezes. ')
