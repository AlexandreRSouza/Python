from math import hypot
cat_oposto = float(input("Digite o comprimento do cateto oposto. "))
cat_adj = float(input('Digite o comprimento do cateto adjacente. '))

#formula sem importação da biblioteca
hip = (cat_oposto ** 2 + cat_adj ** 2) ** (1/2)

print('A hipotenusa é {:.2f}' .format(hip))


#formula com a importação da biblioteca
'''hi = math.hypot(cat_oposto, cat_adj'''
hi = hypot(cat_oposto, cat_adj)


print('A hipotenusa é {:.2f}' .format(hi))


