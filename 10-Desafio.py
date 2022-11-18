#10-Desafio Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. Cons US$1,00=R$3,27#


print('='*20,'Dinheiro','='*20, '\n')
valor = float(input('Valor: R$'))

dolar = valor/3.27

print('Dinheiro convertido em dolar','\n','-'*40)
print('Dolar: {:.2f} US$'.format(dolar))
