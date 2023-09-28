#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

n = int(input('Digite um número. '))
print('''\033[m Digite a base de conversão: 
                 (1) para binário, 
                 (2) para octal,
                 (3) para hexadecimal.''')
base = int(input('Escolha sua opção: '))

if base == 1:
    b = bin(n)
    print('O número {} em binário é {}' .format(n,b[2:]))
elif base == 2:
    o = oct(n)
    print('O número {} em octal é {}' .format(n,o[2:]))
elif base == 3:
    h = hex(n)
    print('O número {} em hexadecimal é {}' .format(n,h[2:]))
else:
    print('Opção Inválida, tente novamente!')
    

