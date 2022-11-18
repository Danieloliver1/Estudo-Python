# 11 Desafio Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-lo, sabendo que cada litro de tinta, pinta uma área de 2m2.

print('-'*10, 'Digite altura e a largura para medir a área em metros',
      '-'*10, '\n', '*'*60)
lar = float(input('Altura em metros: '))
alt = float(input('Largura em metros:'))

area = lar*alt
litro = area/2

print('Area: {:.1f}'.format(area))
print('-'*80, '\n', 'litro de tinta para pintar: ')
print(' Tintas: {:.1f}L'.format(litro))
