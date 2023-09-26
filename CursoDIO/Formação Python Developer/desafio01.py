'''T = input('')

tamanho = len(T)
print(tamanho)

if tamanho > 140:
    print('METT')
else:
    print('TWETT')'''

month = int(input())

months_dict = {1:"january",
               2:"February",
               3:"March",
               4:"April",
               5:"May",
               6:"June",
               7:"July",
               8:"August",
               9:"September",
               10:"October",
               11:"November",
               12:"December",}
               
print(months_dict[month].title())