# 09-Desafio Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

num = int(input('Digite um número inteiro: '))

for c in range(1, 11):
    print('{} x {} = {}'.format(c,num,num*c))
