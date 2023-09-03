altura = float(input('Digite a altura da parede: '))
largura = float(input('Digite a largura da parede: '))
area = altura * largura
tinta = area / 2
'''metroscubicos = area * 100
litros = metroscubicos * 1000
tinta = (200000.0 * 1000)/10000'''
print(" Areá é de {:.2f} m²" .format(area))
print("Para pintar está parede você precisa de {}l de tinta." .format(tinta))




