lado01 = float(input('Digite o primeiro segmento: '))
lado02 = float(input('Digite o segundo segmento: '))
lado03 = float(input('Digite o terceiro segmento: '))

   # Testando se é triângulo
if (lado01 + lado02 < lado03) or (lado01 + lado03 < lado02) or (lado02 + lado03 < lado01):
    print('Os Segmentos Não formam um Triângulo!')
else:
    print('Os Segmentos formam um Triângulo!')
    if lado01 != lado02 != lado03 != lado01:
        print('O Triângulo possui os três lados com medida diferentes, ESCALENO')
    elif lado01 == lado02 == lado03:
        print('O Triângulo possui os três com medida iguais, EQUILÁTERO')
    else:
        print('O Triângulo possui os dois lado iguais, ISÓSCELES')








