# 13-Desafio Faça um algortimo que leia o sálario de um funcionário e mostre seu novo salário, com 15% de aumento.


print('-'*40, 'Salário do funcionário', '-'*40)
sala = float(input('Salário: \nR$'))
aumen = sala*1.15
print('Reajuste de +15%: \nR${:.2f}'.format(aumen))
