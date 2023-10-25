num = cont = soma = 0

while True:
    num = int(input('Digite um número. [Digite 999 para PARAR] '))
    if num == 999:
        break
    else:
        cont = cont + 1 
        soma = soma + num   
print(f'A soma dos {cont} valores é de {soma}.')
