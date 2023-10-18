n1 = int(input('Digite o primeiro termo da P.A. : '))
r = int(input('Digite a razão da P.A. : '))
termo = int(input('Digite o termo da P.A. : '))

a = n1 + (termo - 1) * r #10 - 1 pois vc quer achar o decimo termo, essa é a formula matematica

print("=" *4, '{} termos de uma Progressão Aritmética (P.A.)'.format(termo), "=" *14)

for c in range(n1, a + r, r):
   print(c, end="-")
print('FIM')

#2-5-8-11-14-17-20-23-26-29-FIM




