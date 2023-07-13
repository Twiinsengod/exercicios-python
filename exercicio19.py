# Faça 

import random

n1 = str(input('Primeiro aluno(a): ')) 
n2 = str(input('Segundo aluno(a): ')) 
n3 = str(input('Terceiro aluno(a): ')) 
n4 =str(input('Quarto aluno(a): ')) 
n5 = str(input('Quinto aluno(a): '))
lista = [n1,n2,n3,n4,n5]
escolhido = random.choice(lista)
print('O(a) aluno(a) escolhido(a) foi: {}'.format(escolhido))
