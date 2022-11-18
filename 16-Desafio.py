# 16-Desafio Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção inteira.
import math
num = float(input('Digite um número real qualquer: \n'))

print('valor inteiro do número é {}'.format(math.trunc(num)))
