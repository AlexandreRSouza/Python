import math
cat_oposto = float(input('Digite o valor do cateto oposto: '))
cat_adjacente = float(input('Digite o valor do cateto adjacente: '))
'''x = pow(cat_oposto, 2)
y = pow(cat_adjacente, 2)
hipotenusa = math.sqrt(x + y)'''
hipotenusa = math.hypot(cat_oposto, cat_adjacente)'''importando biblioteca math da hipotenusa'''
print('O Valor da hipotenusa é de {:.2}'.format(hipotenusa))
