nome = input('Digite seu nome: ').strip()#método remove quaisquer espaços em branco iniciais e finais.

print(nome.capitalize())
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(' '))# O .count() retira o que está inidcado dentro dos parenteses.
print(nome.find(' '))#Caso o usuario coloque espaço antes do primeiro nome ele dá o retorno -1.
lista_nome = nome.split() #Divida uma string em uma lista onde cada palavra é um item da lista
print(lista_nome[0])