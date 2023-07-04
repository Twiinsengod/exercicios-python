## Escreva um programa que leia um valor em metros e o exiba covertido em centímetros e milímetros.

metros = int(input("Informe o valor em metros: "))
print("metro(s):", metros)

centimetros = metros * 100
print("O valor em centímetros é: {:.2f}".format(centimetros).replace('.', ','))

milimetros = metros * 1000
print("O valor em milímetros é: {:,}".format(milimetros).replace(',', '.'))
