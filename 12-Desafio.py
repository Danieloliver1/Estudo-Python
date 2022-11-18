# 12-Desafio Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

print('-'*40, 'Preço do produto com desconto', '-'*40)

prod = float(input('Valor do produto: \nR$'))
desco = prod*0.95
print('Produto com desconto: \nR${:.2f}'.format(desco))
