# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dóllares ela pode comprar.
#CONSIDERE US$ 1.00 = R$ 4.82
#CONSIDERE EUR 1.00 = R$ 5.37

real = float(input('Quanto dinheiro você tem na carteira? R$ '))
dolar = real / 4.82
euro = real / 5.37
print('Com R$ {:.2f} você pode comprar US$ {:.2f} dólar(es) e € {:.2f} euro(s)'.format(real, dolar, euro))