sexo = input('Informe seu sexo [M/F] ').strip().upper()

while sexo not in 'MF':
    sexo = input('Dados inválidos, digite novamente, Informe seu sexo [M/F] ').strip().upper()
print('Cadastros do sexo {} realizado com sucesso! '.format(sexo))

