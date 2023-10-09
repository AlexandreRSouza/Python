#lista_nome = []
lista_idades = []
#sexo = []
#lista_todos = []
media_idade = 0
#masc = 0
#fem = 0
maior_idade_homem = 0
nome_velho = ''
total_mulher_20 = 0
for pess in range(1,5):
    print('-------- {}º PESSOA --------'.format(pess))
    nome = input('Digite o nome da {}º pessoa. '.format(pess)).upper().strip()
    idade = int(input('Digite a idade {}º pessoa. '.format(pess)))
    sexo = input('Digite o sexo {}º pessoa, (M) Masculino e (F) Femenino. '.format(pess)).upper().strip()
    lista_idades.append(idade)  # add as idades digitadas na lista
    media_idade = sum(lista_idades) / 4  # fez a media de idade dos usuarios
    if pess == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 'F' and idade < 20:
        total_mulher_20 += 1
print('A media de idade do grupo é de {:.0f} anos. '.format(media_idade))
print('O Homem mais velho é o {} e sua idade é de {} anos.'.format(nome_velho, maior_idade_homem))
print('Ao todo são {} mulheres com menos de 20 anos.'.format(total_mulher_20))



#print('E {} HOMENS e {} MULHERES.'.format(masc, fem))





    #lista_nome.append(nome)#add os nomes digitados na lista
    #lista_idades.append(idade)#add as idades digitadas na lista
    #mais_velho = max(lista_idades)#pegou o maior valor na lista de idade
    #media_idade = sum(media) / 4 #fez a media de idade dos usuarios
    #i = lista_idades.index(mais_velho)
    #i_n = lista_nome[i]
#print(lista_nome)#lista de nomes digitados
#print(lista_idades)#lista de idades digitadas
#print(mais_velho)#o mais velho do grupo
#print(i)#indice do mais velho do grupo
#print('O Mais velho do grupo é o {} com a idade de {} anos.'.format(lista_nome[i], lista_idades[i]))
#print('A media de idade do grupo é de {} anos. .format(media_idade))
