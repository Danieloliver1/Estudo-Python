# 15-Desafio Escreva um programa que pergunte a quantidade de Km percorrido por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 POR Km rodado.

kw = float(input('Quantidade de KW percorrido: \n'))
dias = float(input('Quantidade de dias alugados: \n'))

print('Carro alugado custa R$60 por dia e R$0,15 POR KW percorrido')
print('O carro alugado foram {:.0f}dias custou R${:.2f} \nforam R${:.2f} por KW rodado \ntotal de R${:.2f}'.format(
    dias, dias*60, kw*0.15, (60*dias)+(kw*0.15)))
