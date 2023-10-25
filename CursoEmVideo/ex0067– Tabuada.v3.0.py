cont = mult = 0


while True:
    num = int(input('Digite um número. '))
    if num < 0:
        break
    print('=-' * 20, f'TABUADA DO {num}', '=-' * 20)
    for cont in range(0, 11):
        mult = num * cont
        print(f'{num} x {cont} = {mult} ')
    print('=-' *40)
print('=-' * 20, f'TABUADA ENCERRADA.', '=-' * 20)







