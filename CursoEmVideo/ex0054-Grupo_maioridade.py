from datetime import date
cont = 0
maior = 0
menor = 0
for ano in range(1, 8):
    ano =int(input('Digite o ano que {}º pessoa nasceu. '.format(ano)))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print('{} pessoas são MAIOR DE IDADE'.format(maior))
print('{} pessoas são MENOR DE IDADE'.format(menor))




