num = int(input('Digite um número. '))

t1= 0
t2 = 1
cont = 3

print('{} - {} -'.format(t1, t2),end='')
while cont <= num:    
    t3 = t1 + t2
    print(' {} - '.format(t3),end='')
    t1 = t2
    t2 = t3
    cont += 1
print('FIM')





