#faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

Ca = float(input('Qual é o valor do comprimento do cateto oposto? '))
Co = float(input('Qual é o valor do comprimento do cateto adjacente? '))

hi = (Co ** 2 + Ca ** 2) ** (1/2)
print('O valor da hipotenusa é: {:.2f}'.format(hi))