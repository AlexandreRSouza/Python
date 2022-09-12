'''import math
angulo = float(input('Digite o ângulo: '))
o Seno, cosseno e tangente com resultado em radianos e preciso fazer a conversão de radianos para grau.
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print("O angulo de {}º tem o seno = {:.2} cosseno = {:.2} e tangente = {:.2}".format(angulo, seno, cosseno, tangente))'''


from math import radians,cos,sin,tan
ângulo = float(input('Digite o ângulo: '))
seno = sin(radians(ângulo))
print('O ângulo de {}º tem o seno de {:.2}'.format(ângulo, seno))
cosseno = cos(radians(ângulo))
print('O ângulo de {}º tem o cosseno de {:.2}'.format(ângulo, cosseno))
tangente = tan(radians(ângulo))
print('O ângulo de {}º tem a tangente de {:.2}'.format(ângulo, tangente))