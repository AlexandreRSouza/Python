produto = float(input('Digite o preço do Produto em R$ '))

desconto = (produto * 5) / 100
preço_atual = produto - desconto

print('O produto inicial custa R$ {} com desconto de 5% sai por R$ {:.2f}' .format(produto, preço_atual))