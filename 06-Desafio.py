# 06-Desafio
# Crie um algoratimo que leia um
# número e mostre o seu dobro, triplo e raiz quadrada.

numero = float(input('Digite um número: '))

dobro = numero * 2
triplo = numero * 3
rquadrada = numero**(1/2)

print('O número {:.2f} seu dobro é {:.2f} e seu triplo é {:.2f} e raíz quadrada de {:.2f} é {:.2f} .'.format(
    numero, dobro, triplo, numero, rquadrada))
