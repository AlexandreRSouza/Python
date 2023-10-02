'''Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.'''
from datetime import date
'''print(date.today().day)
print(date.today().month)
print(date.today().year)'''

ano_nascimento = int(input('Digite o ano de nascimento. '))
sexo = str(input('Digite seu sexo.')).upper()

idade = date.today().year - ano_nascimento
if sexo == 'F':
    print('Você é do sexo Femino, não precisa se alistar!')
elif idade == 18:
    print('Você tem {} anos de idade.'.format(idade))
    print('Hora de alistar no serviço militar.')
elif idade < 18:
    falta = 18 - idade
    print('Você tem {} anos de idade.'.format(idade))
    print('Falta {} ano(s) para poder fazer o alistamento militar.'.format(falta))
    print('Seu alistamento será {}.'.format(ano_nascimento + falta))
else:
    passou = idade - 18
    print('Você tem {} anos de idade.'.format(idade))
    print('você passou {} ano(s) para pode fazer o alistamento militar.'.format(passou))
    print('Seu alistamento foi em {}'.format(ano_nascimento + 18))



