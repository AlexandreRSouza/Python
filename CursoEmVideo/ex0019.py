#programa para sortear um nome da lista
# dois modos, um já com a lista criada e outro com entrada de dados e criando a lista

import random

alunos = ['Alexandre', 'Maria', 'João', 'Luis', 'Ana', 'José']

sorteio = random.choice(alunos)


aluno1 = input('Digite o primeiro aluno. ')
aluno2 = input('Digite o segundo aluno. ')
aluno3 = input('Digite o terceiro aluno. ')
aluno4 = input('Digite o quarto aluno. ')

alu = [aluno1, aluno2, aluno3, aluno4]

sortudo = random.choice(alu)


print(sorteio)
print(sortudo)
