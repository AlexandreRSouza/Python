frase = input('Digite uma frase: ') .strip().upper()#retirar os espaços inicias/finais e colocar a frase toda em maiuscula
palavras = frase.split()#separa a frase digitada pelo usúario pelos espaços criando uma lista
junto = ''.join(palavras) #juntando a lista
inverso = ''

for letra in range(len(junto) -1, -1, -1):#pegou o tamanho da variavel junto indo do inicio até a ultima letra -1 para poder pegar todas a letras
   inverso += junto[letra]
print(junto, inverso)
if junto == inverso:
   print('Sua Frase é um palíndrome')
else:
   print('Não é um Palíndrome')










