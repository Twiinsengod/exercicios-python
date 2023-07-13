# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la. Sabendo que cada litro de tinta pinta uma área de 2m²

larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
area = alt * larg
tinta = area / 2
print('A sua parede tem a dimensão de {} x {} e sua área é de {} m²'.format(larg,alt,area))
print('Você precisa de {} litros de tinta para pintar uma parede de {} m²'.format(tinta,area))


