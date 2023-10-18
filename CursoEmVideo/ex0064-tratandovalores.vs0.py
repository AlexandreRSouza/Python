num = ''
total = 0
dig = 0
num = int(input('Digite um valor inteiro. [999 para parar]. '))
while num != 999:    
    total += num
    dig += 1
    num = int(input('Digite um valor inteiro. [999 para parar]. '))
print('Você digitou {} vezes'.format(dig))
print('A Soma total foi de {}'.format(total))





