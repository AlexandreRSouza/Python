peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc < 18.5:
    print('Sei IMC é de {:.2f}, Abaixo do Peso' .format(imc))
elif 18.5 <= imc < 25:
    print('Sei IMC é de {:.2f}, Peso Ideal' .format(imc))
elif 25 <= imc < 30:
    print('Sei IMC é de {:.2f}, Sobrepeso'.format(imc))
elif 30 <= imc < 40:
    print('Sei IMC é de {:.2f},Obesidade'.format(imc))
else:
    print('Sei IMC é de {:.2f}, Obesidade Mórbida'.format(imc))




