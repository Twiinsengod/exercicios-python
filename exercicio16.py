# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela a sua porção  inteira.

'''import math (COM IMPORTAÇÃO DE BIBLIOTECA)

n1 = float(input('Digite um número: '))
print('A porção inteira de {} é {}'.format(n1, math.trunc(n1)))'''



num = float(input('Digite um valor: ')) #sem importar biblioteca
print('A porção inteira de {} é {}'.format(num,int(num)))