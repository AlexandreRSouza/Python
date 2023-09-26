nome = str(input('Digite seu nome completo. ')).strip()
lista_nome = nome.split()

print('Seu nome completo: {} ' .format(nome))
print('Seu primeiro nome é: {}'.format(lista_nome[0]))
print('Seu ultimo nome é: {}'.format(lista_nome[-1]))