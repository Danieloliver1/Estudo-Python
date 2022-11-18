import tabnanny


print('='*20, 'Desafio 04', '='*20)

n1 = input('Digite qualquer coisa: ')


print('Seja bem vindo {}'.format(n1))
print('O tipo primitivo é ', type(n1))
print('Só tem espaço? ', n1.isspace())
print('É um número? ', n1.isnumeric())
print('É alfabético? ', n1.isalpha())
print('É alfanumérico? ', n1.isalnum())
print('Estar em maiúscula? ', n1.isupper())
print('Estar em minúscula? ', n1.islower())
# Ou seja contem maiúscula e minúscula.
print('Estar capitalizada? ', n1.istitle())

# Os caracteres alfanuméricos contêm a mistura dos 26
# caracteres do conjunto de letras e os números de 0 a 9.
# Os caracteres não alfanuméricos incluem os caracteres
# que não são letras ou dígitos, como + e @ .
