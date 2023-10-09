n = int(input('Digite um número. '))

print("=-" * 2,'TABUADA', "=-" * 2)

for c in range(0, 11):
   print('{} x {:2} = {:2} '.format(n, c, n * c))