import math

num = float(input('Digite um ângulo qualquer. '))

num_rad = math.radians(num)
print(num_rad)

coseno = math.cos(num_rad)
seno = math.sin(num_rad)
tang = math.tan(num_rad)

print('O Cosseno de {}° é de {:.2f}' .format(num, coseno))
print('O Seno de {}° é de {:.2f}' .format(num, seno))
print('A tangente de {}º é de {:.2f}' .format(num, tang))


