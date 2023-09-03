#programa para indentifica se o nome tem Silva dentro do nome.
nome=str(input('Qual seu nome completo? ')).strip()
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))
