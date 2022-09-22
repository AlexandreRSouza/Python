nome=str(input('Digite seu nome completo: ')).strip()
print('Nome Letras maiúsculas {}'.format(nome.upper()))
print('Nome letras minúsculas {}'.format(nome.lower()))
print('Quantas letrasa ao todo (sem considerar espaços) {}'.format(len(nome)-nome.count(' ')))
#print('Quantos letras tem o primeiro nome {}'.format(nome.find(' ')))
separa=nome.split()#separar nome dentro de uma lista
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))