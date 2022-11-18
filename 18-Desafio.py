# 18-Desafio faça um programa que leia um ângulo qualquer e mostre na tela o valor ddo seno, cosseno e tangente desse ângulo.

import math
ang = float(input('Digite valor do angulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))

print('Seno     {:.4f}\nCosseno  {:.4f}\nTangente {:.4f}\n'.format(sen,cos,tan))


