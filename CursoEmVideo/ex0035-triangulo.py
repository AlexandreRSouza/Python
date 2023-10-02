a = float(input('Primeiro lado: '))
b = float(input('Segundo  lado: '))
c = float(input('Terceiro lado: '))
    
    # Testando se é triângulo
if (a + b < c) or (a + c < b) or (b + c < a):
    print('\033[7;31;41mNao é um triangulo\033[m')
else:
    print('As 3 retas formam um triângulo!')
