numero = int(input('Digite um número entre 0 e 9999 '))

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10

print('A unidade é {}' .format(u))
print('A dezena é {}' .format(d))
print('A centena é {}' .format(c))
print('A milhar é {}' .format(m))


