# 17-Desafio faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da hipotenusa.

import math

cat1 = float(input('Cateto Oposto: \n'))
cat2 = float(input('CatetoAdjacente: \n'))

cat1 = math.pow(cat1, 2)
cat2 = math.pow(cat2, 2)
hip = math.sqrt(cat1+cat2)

print('Hipotenusa {:.0f}\ncateto oposto {:.0f}\ncateto adjacente {:.0f}'.format(
    hip, cat1, cat2))
