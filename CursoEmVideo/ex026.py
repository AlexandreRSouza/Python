frase = str(input('Digite uma frase: ')).upper().strip()

print('A palavra aparece {} vezes.'.format(frase.count('A')))#conta quantas vezes o carctere aparece
print('A primeira letra A/a aparece na posição {}.' .format(frase.find('A')+1))
print('A ultima letra A/a parece na posição {}.'.format(frase.rfind('A')+1))




