from datetime import date
nascimento = int(input('Digite o ano do seu nascimento: '))

idade = date.today().year - nascimento

if idade <= 9:
    print('Sua idade é de {} anos, você é um Atleta Mirim!'.format(idade))
elif idade > 9 and idade <= 14:
    print('Sua idade é de {} anos, você é um Atleta Infantil!'.format(idade))
elif idade > 14 and idade <= 19:
    print('Sua idade é de {} anos, você é um Atleta Júnior!'.format(idade))
elif idade > 19 and idade <= 25:
    print('Sua idade é de {} anos, você é um Atleta Sênior!'.format(idade))
else:
    print('Sua idade é de {} anos, você é um Atleta Master!'.format(idade))







