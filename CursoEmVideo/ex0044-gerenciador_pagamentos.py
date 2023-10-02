preco = float(input('Qual o Preço do Produto? R$ '))
forma_pagamento = int(input('''Qual a forma de pagamento: 
                            [1] à vista dinheiro/cheque: 10% de desconto
                            [2] à vista no cartão: 5% de desconto
                            [3] em até 2 x no cartão: preço formal
                            [4] 3x ou mais no cartão: 20% de Juros
                            '''))

if forma_pagamento == 1:
    valor = preco - (preco * 10 / 100)
    print('O valor do produto é de R${:.2f} com desconto de 10% foi para R$ {:.2f}'.format(preco, valor))
elif forma_pagamento == 2:
    valor = preco - (preco * 5 / 100)
    print('O valor do produto é de R${:.2f} com desconto de 5% foi para R$ {:.2f}'.format(preco, valor))
elif forma_pagamento == 4:
    parcela = int(input('Quantas vezes vai parcelar, quantidade mínima de 3 vezes. '))
    valor = preco + (preco * 20 / 100)    
    parcela_atual = valor / parcela
    print('O valor do produto é de R${:.2f} com o juros de 20% foi para R$ {:.2f} e dividido em {} sua parcela é de R$ {}'.format(preco, valor, parcela, parcela_atual))
elif forma_pagamento == 3:
    valor = preco / 2
    print('o valor da parcela em 2x é de R$ {:.2f}'.format(valor))
    print('O valor do produto é de R${:.2f}'.format(preco))
else:
    print('Opção inválida!')















