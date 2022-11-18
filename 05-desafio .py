#Desafio-05 faça um programa que leia mum  número interiro e mostre na tela o seu sucessor e seu antecessor.#

numero = int(input(" Digite um número inteiro: "))

antercessor = numero - 1
sucessor = numero + 1

print('Antercessor de {:.1f} é {:.1f} '.format(numero, antercessor))
print('Sucesoor de {:.1f} é {:.1f} '.format(numero, sucessor))
