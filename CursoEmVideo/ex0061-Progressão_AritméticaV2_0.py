num = int(input('Digite o primeiro termo da P.A. '))
r = int(input('Digite a razão da P.A. '))
#termo = int(input('Digite o termo da P.A. '))

a = 1
termo = num

print("=" *4, '{} termos de uma Progressão Aritmética (P.A.)'.format(termo), "=" *14)

while a <= 10:
    print('{} - '.format(termo), end='')
    termo += r
    a += 1
print('FIM')

