from random import randint
from time import sleep

pc = randint(0,5)

numero = int(input('Digite um número de 0 a 5. '))

print('Processando...')
sleep(3)

if numero == pc:
    print('PARABÉNS, VOCÊ GANHOU!')
else:
    print('VOCÊ PERDEU! GAME OVER')
