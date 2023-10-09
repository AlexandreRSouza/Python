lista_peso = [] #criando uma lista vazia
for pess in range(1, 6):
    peso = float(input('Qual é o Peso da {}º pessoa? '.format(pess)))
    lista_peso.append(peso) #inserindo na lista a entrada de peso dos usuário
    lista_peso.sort()#ordenando a lista em ordem crescente
print('O Maior Peso foi de {:.2f} KG'.format(lista_peso[-1]))
print('O Menor Peso foi de {:.2f} KG'.format(lista_peso[0]))
