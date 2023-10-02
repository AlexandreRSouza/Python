'''Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais'''

num01 = int(input('Digite o primeiro número: '))
num02 = int(input('Digite o segundo número: '))

if num01 > num02:
    print('O primeiro número é maior.')
elif num02 > num01:
    print('O segundo número é maior.')
else:
    print('Os números são iguais!')



