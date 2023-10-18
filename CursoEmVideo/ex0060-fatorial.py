num = int(input('Digite um número. '))
c = num
fat = 1

'''for n in range(1, num+1):
    fat = fat * n
print(fat)'''

print('O Fatorial de {}! ='.format(num),end=' ')
while c > 0:
    print('{}'.format(c),end='')
    print(' x ' if c > 1 else ' = ',end='')
    fat = fat * c
    c -= 1
print(fat)



