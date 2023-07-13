# Faça um algorítmo que leia o preço de um produto e mostre seu novo preço com %5 de desconto.

preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 5 / 100)
print('O produto passará a valer R$ {:.2f} ao aplicar 5% de desconto'.format(novo))