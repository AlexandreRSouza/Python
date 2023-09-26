a = int(input('Digite o primeiro número: '))
b = int(input('Digite o segunda número: '))
c = int(input('Digite o terceiro número: '))



if b > c and b > a:
    print('O maior número é : {}'.format(b))
if c > b and c > a:
    print('O maior número é : {}'.format(c))
else:
    print('O maior número é : {}'.format(a))

if b < c and b < a:
    print('O maior número é : {}'.format(b))
if c < b and c < a:
    print('O maior número é : {}'.format(c))
else:
    print('O maior número é : {}'.format(a))

