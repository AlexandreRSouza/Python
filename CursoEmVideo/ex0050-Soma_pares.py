soma = 0
cont = 0
for num in range(1, 7):
    num = int(input('Digite um número. '))
    if num % 2 == 0:
        soma = soma + num
        cont = cont + 1
print('Você digitou {} números e deles {} são pares, a soma foi de {}'.format(num, cont, soma))








