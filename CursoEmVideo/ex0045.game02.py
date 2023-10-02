import random
from time import sleep
usuario = int(input('''Escolha uma Opção:
                    [1] Pedra, 
                    [2] Papel,
                    [3] Tesoura. '''))

print("=-" * 20)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!!')
sleep(1)

print("=-" * 20)

game = ['Pedra' , 'Papel', 'Tesoura']
pc_game = random.choice(game)


if usuario == 1 and pc_game == 'Tesoura':
    print('o PC_GAMER jogou! {} e Você Jogou Pedra'.format(pc_game))
    print('Você Ganhou!')
elif usuario == 1 and pc_game == 'Papel':
    print('o PC_GAMER jogou! {} e Você Jogou Pedra'.format(pc_game))
    print('Você Perdeu!')
elif usuario == 1 and pc_game == 'Pedra':
    print('Empatou! O PC_GAMER jogou {} E O USUÁRIO jogou {}  '.format(pc_game, pc_game))
elif usuario == 2 and pc_game == 'Tesoura':
    print('o PC_GAMER jogou! {} e Você Jogou Papel'.format(pc_game))
    print('Você Perdeu!')
elif usuario == 2 and pc_game == 'Pedra':
    print('o PC_GAMER jogou! {} e Você Jogou Papel'.format(pc_game))
    print('Você Ganhou!')
elif usuario == 2 and pc_game == 'Papel':
    print('Empatou! O PC_GAMER jogou {} E O USUÁRIO jogou {}  '.format(pc_game, pc_game))
elif usuario == 3 and pc_game == 'Papel':
    print('o PC_GAMER jogou! {} e Você Jogou Tesoura'.format(pc_game))
    print('Você Ganhou!')
elif usuario == 3 and pc_game == 'Pedra':
    print('o PC_GAMER jogou! {} e Você Jogou Tesoura'.format(pc_game))
    print('Você Perdeu!')    
elif usuario == 3 and pc_game == 'Tesoura':
    print('Empatou! O PC_GAMER jogou {} E O USUÁRIO jogou {}  '.format(pc_game, pc_game))
else:
    print('Opção Inválida!')























