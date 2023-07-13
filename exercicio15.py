# Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.Calcule o preço a pagar (sabendo que o carro custa R$ 60/dia e R$0.15 por KM rodado).

dias = int(input('O carro foi alugado por quantos dias? '))
km = float(input('Quantos KM foram rodados? '))
pago = (dias * 60) + (km * 0.15) 


print('O total à pagar é de R$ {:.2f}'.format(pago))


