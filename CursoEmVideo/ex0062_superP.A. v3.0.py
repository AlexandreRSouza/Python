n1 = int(input('Digite o primeiro Termo da P.A. '))
razao = int(input('Digite a razão da P.A. '))
quant = int(input('Digite quantos números mostrar na P.A. '))
c = 0
termo = n1
mais = quant
total = 0

print("=" *4, '{} termos de uma Progressão Aritmética (P.A.)'.format(termo), "=" *14)
while mais != 0:
    total = total + mais
    while c < total:
        print('{} - '.format(termo), end='')
        termo = termo + razao
        c = c + 1
    print('PAUSA')
    print('=-' *40)
    mais = int(input('Deseja digitar mais termos para P.A. '))
print('P.A. concluída, o total de termos foi de {}'.format(total))



