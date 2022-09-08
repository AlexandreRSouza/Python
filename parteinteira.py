''' Primeira forma importando a biblioteca

from math import trunc
num = float(input('Digite um número real: '))
print('O numero digitado foi {} e sua parte inteira é {}'.format(num, trunc(num)))'''



'''Sem importar a biblioteca'''
num = float(input('Digite um valor: '))
print('O número digitado foi {} e sua porção inteira é {}'.format(num,int(num)))
