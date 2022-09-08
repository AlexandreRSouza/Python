preço = float(input("Digite o valor do produto R$ "))
desconto = (preço * 5)/100
desconto_total = preço - desconto
print('O valor do produto é de R$ {:.2f} com desconto de 5% o preço atualizado é de R$ {:.2f}' .format(preço,desconto_total))
