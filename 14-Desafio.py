# 14-Desafio Crie um programa que leia a temperatura em graus celsius e transforme em fahrenheit


print('-'*20, 'Temperatura', '-'*20)
c = float(input('Digite o valor da temperatura em celsius: \n'))

print('A conversão em Fahrenheit: \n {:.2f}'.format((c*1.8)+32))
