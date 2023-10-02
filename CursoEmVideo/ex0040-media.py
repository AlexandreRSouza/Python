nota01 = float(input('Digite a primeira nota: '))
nota02 = float(input('Digite a segunda nota: '))

media = (nota01 + nota02) / 2

if media < 5.0:
    print('Sua média foi de {}, Está REPROVADO!'.format(media))
elif media >= 7.0:
    print('Sua média foi de {}, Está APROVADO!'.format(media))
else:
    print('Sua média foi de {}, Está em RECUPERAÇÃO!'.format(media))

