from random import randint
from time import sleep

pc_gamer =randint(0,10)
print(pc_gamer)

jogadas = 0

print('------- ACERTE O NÚMERO QUE ESTOU PENSANDO -------')
jogador = int(input('Adivinhe o número entre 0 e 10 '))
jogadas += 1

while jogador != pc_gamer:
    if jogador > pc_gamer:
        print('.', end='')
        sleep(1)
        print('..', end='')
        sleep(1)
        print('...')
        sleep(1)
        print('??????')
        sleep(1)
        print('ERROU!')
        jogador = int(input('Menor valor! \n Jogue novamente entre 0 e 10 '))
        jogadas += 1
    else:
        print('.', end='')
        sleep(1)
        print('..', end='')
        sleep(1)
        print('...')
        sleep(1)
        print('??????')
        sleep(1)
        print('ERROU!')
        jogador = int(input('Maior valor! \n Jogue novamente entre 0 e 10 '))
        jogadas += 1
print('.',end='')
sleep(1)
print('..',end='')
sleep(1)
print('...')
sleep(1)
print('??????')
sleep(1)
print('GANHOU!!!!')
sleep(1)
print('O PC_GAMER jogou {} e Você jogou {}'.format(pc_gamer, jogador))
if jogadas == 1:
    print('PARABÉNS, ACERTOU NA PRIMEIRA!!!!')
else:
    print('Você precisou de {} jogadas para acertar!'.format(jogadas))


