# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF

celsius = float(input('Digite o valor em ºC: '))
farenheit = celsius + (0 * 9/5) + 32
kelvin = celsius + (273.15)

print('A temperatura (em Farenheit) é de {:.2f}ºF'.format(farenheit))
print('A temperatura (em Kelvin) é de {:.2f}ºK'.format(kelvin))
if celsius <= 0:
    print('Risco de hiportemia. Procure uma fonte de calor imediatamente!')
elif celsius < 15:
    print('A temperatura está baixa. Agasalhe-se!')
elif celsius > 25:
    print('Hidrate-se e fique na sombra. A temperatura está alta!')
if celsius >= 30:
    print('Risco de insolação. Procure hidratar-se imediatamente!')