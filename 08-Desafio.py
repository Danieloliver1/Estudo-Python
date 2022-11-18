# 08-Desafio um programa que leia um valor em metros e o exiba convertido em centimentros e milimetros.

valor = float(input('Digite o valor em metros :'))
print('valor convertido em centimentros é {:.0f}cm'.format(valor*100))
print('valor convertido em milimetros é {:.0f}mm'.format(valor*1000))
