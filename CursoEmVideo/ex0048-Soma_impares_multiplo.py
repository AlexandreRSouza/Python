'''Podemos representar a fórmula geral para encontrar o múltiplo de um número como:

reto b espaço igual a espaço reto a espaço. espaço reto k

Onde,

    b é o múltiplo
    a é um número natural
    k é um número natural qualquer'''

'''soma = 0
cont = 0'''


n = int(input('Digite um número para saber quais seus multiplos.'))
soma = 0
cont = 0
for c in range(1, 501, 2):
    c = n * c
    if c % 3 == 0:
        print('{}'.format(c), end=" ")
        soma = soma + c
        cont = cont + 1
print('A soma dos {} valores é de {}'.format( cont,soma))

soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A Soma dos {} valores é de {}'.format(cont, soma))